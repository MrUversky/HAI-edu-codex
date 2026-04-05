#!/usr/bin/env python3
"""Thin Telegram adapter for the workshop starter repo."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


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


def read_message(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8").strip()
    return sys.stdin.read().strip()


def write_dry_run(path: str, payload: dict) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def send_message(token: str, chat_id: str, text: str) -> dict:
    body = json.dumps({"chat_id": chat_id, "text": text}).encode("utf-8")
    req = Request(
        url=f"https://api.telegram.org/bot{token}/sendMessage",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(req, timeout=20) as resp:
        data = resp.read().decode("utf-8")
    return json.loads(data)


def main() -> int:
    parser = argparse.ArgumentParser(description="Send or dry-run a Telegram message.")
    parser.add_argument("--message-file", help="Path to a UTF-8 text file with the message body.")
    parser.add_argument("--dry-run-path", required=True, help="Where to save dry-run payload if live send is unavailable.")
    parser.add_argument("--force-dry-run", action="store_true", help="Skip live send and only save the payload.")
    args = parser.parse_args()

    text = read_message(args.message_file)
    if not text:
        raise SystemExit("Message is empty.")

    load_env_local()
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    payload = {
        "status": "dry-run",
        "chat_id": chat_id or "",
        "text": text,
    }

    if args.force_dry_run or not token or not chat_id:
        write_dry_run(args.dry_run_path, payload)
        print(json.dumps(payload, ensure_ascii=False))
        return 0

    try:
        response = send_message(token, chat_id, text)
    except (HTTPError, URLError, TimeoutError) as exc:
        payload["error"] = str(exc)
        write_dry_run(args.dry_run_path, payload)
        print(json.dumps(payload, ensure_ascii=False))
        return 0

    print(json.dumps({"status": "sent", "response": response}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
