#!/usr/bin/env python3
"""Download a Gmail attachment using a local OAuth flow."""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import secrets
import threading
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlencode, urlparse, parse_qs

import requests


SCOPE = "https://www.googleapis.com/auth/gmail.readonly"
TOKEN_FILE = Path(".gmail-token.json")
REDIRECT_URI = "http://127.0.0.1:8765/callback"


def load_env_local() -> None:
    env_file = Path(".env.local")
    if not env_file.exists():
        return
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if key and key not in os.environ:
            os.environ[key] = value


def get_client_config() -> tuple[str, str]:
    load_env_local()
    client_id = os.getenv("GMAIL_CLIENT_ID")
    client_secret = os.getenv("GMAIL_CLIENT_SECRET")
    if not client_id or not client_secret:
        raise SystemExit(
            "Missing GMAIL_CLIENT_ID or GMAIL_CLIENT_SECRET. Put them in env vars or .env.local."
        )
    return client_id, client_secret


def save_token(data: dict[str, Any]) -> None:
    TOKEN_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_token() -> dict[str, Any] | None:
    if TOKEN_FILE.exists():
        return json.loads(TOKEN_FILE.read_text(encoding="utf-8"))
    return None


def refresh_token(token_data: dict[str, Any], client_id: str, client_secret: str) -> dict[str, Any]:
    refresh = token_data.get("refresh_token")
    if not refresh:
        raise SystemExit("Token exists but has no refresh_token. Re-run auth flow.")
    resp = requests.post(
        "https://oauth2.googleapis.com/token",
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh,
            "grant_type": "refresh_token",
        },
        timeout=30,
    )
    resp.raise_for_status()
    fresh = resp.json()
    fresh["refresh_token"] = refresh
    fresh["expires_at"] = time.time() + int(fresh.get("expires_in", 0))
    save_token(fresh)
    return fresh


def get_valid_token(client_id: str, client_secret: str) -> str:
    token_data = load_token()
    if token_data and token_data.get("access_token") and token_data.get("expires_at", 0) > time.time() + 60:
        return token_data["access_token"]
    if token_data and token_data.get("refresh_token"):
        return refresh_token(token_data, client_id, client_secret)["access_token"]
    return run_auth_flow(client_id, client_secret)["access_token"]


def run_auth_flow(client_id: str, client_secret: str) -> dict[str, Any]:
    auth_code_holder: dict[str, str] = {}
    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode("utf-8")).digest()).rstrip(b"=").decode("utf-8")

    class CallbackHandler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802
            parsed = urlparse(self.path)
            params = parse_qs(parsed.query)
            if "code" in params:
                auth_code_holder["code"] = params["code"][0]
                body = b"Gmail auth received. You can return to Codex."
                self.send_response(200)
                self.send_header("Content-Type", "text/plain; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            else:
                body = b"Gmail auth failed."
                self.send_response(400)
                self.send_header("Content-Type", "text/plain; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

        def log_message(self, format: str, *args: object) -> None:  # noqa: A003
            return

    server = HTTPServer(("127.0.0.1", 8765), CallbackHandler)
    thread = threading.Thread(target=server.handle_request, daemon=True)
    thread.start()

    auth_url = "https://accounts.google.com/o/oauth2/v2/auth?" + urlencode(
        {
            "client_id": client_id,
            "redirect_uri": REDIRECT_URI,
            "response_type": "code",
            "scope": SCOPE,
            "access_type": "offline",
            "prompt": "consent",
            "code_challenge": challenge,
            "code_challenge_method": "S256",
        }
    )

    print("Open this URL in your browser to authorize Gmail attachment access:")
    print(auth_url)
    try:
        webbrowser.open(auth_url)
    except Exception:
        pass

    deadline = time.time() + 180
    while "code" not in auth_code_holder and time.time() < deadline:
        time.sleep(0.5)
    server.server_close()
    if "code" not in auth_code_holder:
        raise SystemExit("Timed out waiting for Gmail OAuth callback.")

    resp = requests.post(
        "https://oauth2.googleapis.com/token",
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "code": auth_code_holder["code"],
            "grant_type": "authorization_code",
            "redirect_uri": REDIRECT_URI,
            "code_verifier": verifier,
        },
        timeout=30,
    )
    resp.raise_for_status()
    token_data = resp.json()
    token_data["expires_at"] = time.time() + int(token_data.get("expires_in", 0))
    save_token(token_data)
    return token_data


def download_attachment(access_token: str, message_id: str, attachment_id: str) -> bytes:
    url = f"https://gmail.googleapis.com/gmail/v1/users/me/messages/{message_id}/attachments/{attachment_id}"
    resp = requests.get(url, headers={"Authorization": f"Bearer {access_token}"}, timeout=30)
    resp.raise_for_status()
    payload = resp.json()
    data = payload.get("data")
    if not data:
        raise SystemExit("Attachment response had no data field.")
    padded = data + "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(padded.encode("utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Download a Gmail attachment to a local file.")
    parser.add_argument("message_id")
    parser.add_argument("attachment_id")
    parser.add_argument("filename")
    parser.add_argument("--output-dir", default="drafts/demo/attachments")
    args = parser.parse_args()

    client_id, client_secret = get_client_config()
    token = get_valid_token(client_id, client_secret)
    content = download_attachment(token, args.message_id, args.attachment_id)

    target_dir = Path(args.output_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / args.filename
    target.write_bytes(content)
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
