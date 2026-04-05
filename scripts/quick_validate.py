#!/usr/bin/env python3
"""Run a lightweight workshop sanity check for a generated skill."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "Goal",
    "Inputs",
    "Outputs",
    "Success Criteria",
    "Out of Scope",
    "Procedure",
    "Human Review",
    "Example Usage",
]

SUSPICIOUS_INTEGRATIONS = [
    "slack",
    "notion",
    "jira",
    "salesforce",
    "hubspot",
    "postgres",
    "airtable",
]


def extract_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        raise ValueError("Missing YAML frontmatter start.")
    try:
        _, frontmatter, body = text.split("---", 2)
    except ValueError as exc:
        raise ValueError("Malformed YAML frontmatter.") from exc
    data: dict[str, str] = {}
    for raw_line in frontmatter.strip().splitlines():
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        data[key.strip()] = value.strip()
    return data, body


def validate_paths(text: str) -> list[str]:
    warnings: list[str] = []
    for match in re.findall(r"`([^`]+(?:\.py|\.md))`", text):
        if match.startswith(("drafts/", "outputs/", "participants/")):
            continue
        if "/" in match and not Path(match).exists():
            warnings.append(f"Referenced path does not exist: {match}")
    return warnings


def validate_integrations(text: str) -> list[str]:
    lowered = text.lower()
    warnings: list[str] = []
    for name in SUSPICIOUS_INTEGRATIONS:
        if name in lowered:
            warnings.append(f"Check external integration claim manually: {name}")
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Workshop sanity check for a skill.")
    parser.add_argument("skill_path", help="Path to SKILL.md")
    args = parser.parse_args()

    skill_path = Path(args.skill_path)
    if not skill_path.exists():
        raise SystemExit(f"File does not exist: {skill_path}")

    text = skill_path.read_text(encoding="utf-8")
    issues: list[str] = []
    warnings: list[str] = []

    try:
        frontmatter, body = extract_frontmatter(text)
    except ValueError as exc:
        issues.append(str(exc))
        frontmatter, body = {}, text

    if "name" not in frontmatter:
        issues.append("Frontmatter must include `name`.")
    if "description" not in frontmatter:
        issues.append("Frontmatter must include `description`.")

    for section in REQUIRED_SECTIONS:
        if f"## {section}" not in body:
            issues.append(f"Missing required section: {section}")

    warnings.extend(validate_paths(text))
    warnings.extend(validate_integrations(text))

    print(f"Quick validate: {skill_path}")
    if issues:
        print("Status: FAIL")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("Status: PASS")
        print("- Workshop contract looks complete.")

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")

    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
