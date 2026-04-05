#!/usr/bin/env python3
"""Normalize a generated workshop skill to the repo contract."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def extract_body(text: str) -> str:
    if text.startswith("---\n"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2].lstrip("\n")
    for marker in ("\n# ", "# "):
        idx = text.find(marker)
        if idx >= 0:
            return text[idx + 1 :] if marker.startswith("\n") else text[idx:]
    return text.lstrip()


def normalize_text(text: str, name: str, description: str) -> str:
    body = extract_body(text)
    frontmatter = "\n".join(
        [
            "---",
            f"name: {name}",
            f"description: {description}",
            "---",
            "",
        ]
    )
    return frontmatter + body.lstrip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize generated SKILL.md frontmatter.")
    parser.add_argument("skill_path", help="Path to generated SKILL.md")
    parser.add_argument("--name", required=True, help="Canonical skill name")
    parser.add_argument("--description", required=True, help="Canonical skill description")
    args = parser.parse_args()

    skill_path = Path(args.skill_path)
    if not skill_path.exists():
        raise SystemExit(f"File does not exist: {skill_path}")

    name = slugify(args.name)
    if not name:
        raise SystemExit("Normalized skill name is empty.")

    original = skill_path.read_text(encoding="utf-8")
    normalized = normalize_text(original, name, args.description.strip())
    skill_path.write_text(normalized, encoding="utf-8")
    print(skill_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
