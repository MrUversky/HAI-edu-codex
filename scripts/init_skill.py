#!/usr/bin/env python3
"""Create a workshop skill skeleton for this repository."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


SECTIONS = [
    "Goal",
    "Inputs",
    "Outputs",
    "Success Criteria",
    "Out of Scope",
    "Procedure",
    "Human Review",
    "Example Usage",
]


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def build_skill_md(name: str, description: str) -> str:
    title = name.replace("-", " ").title()
    lines = [
        "---",
        f"name: {name}",
        f"description: {description}",
        "---",
        "",
        f"# {title}",
        "",
    ]
    for section in SECTIONS:
        lines.extend([f"## {section}", ""])
        if section == "Goal":
            lines.append("Коротко опиши, какую повторяемую задачу решает skill.")
        elif section == "Inputs":
            lines.extend(["- какой основной вход", "- какие файлы или источники используются"])
        elif section == "Outputs":
            lines.append("- какой файл или артефакт должен получиться")
        elif section == "Success Criteria":
            lines.append("- по каким признакам понятно, что skill сработал хорошо")
        elif section == "Out of Scope":
            lines.append("- что skill специально не делает")
        elif section == "Procedure":
            lines.extend(
                [
                    "1. Опиши шаги кратко и по делу.",
                    "2. Не делай слишком много магии.",
                    "3. Не смешивай skill с отдельной интеграцией без необходимости.",
                ]
            )
        elif section == "Human Review":
            lines.append("Опиши, где человек должен посмотреть результат или подтвердить draft.")
        else:
            lines.append("`Короткая команда, с которой этот skill логично вызывать`")
        lines.extend(["", ""])
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a workshop skill skeleton.")
    parser.add_argument("name", help="Skill name, for example extract-meeting-actions")
    parser.add_argument("description", help="One-sentence skill description")
    parser.add_argument(
        "--target-root",
        default=".agents/skills",
        help="Root directory for created skills (default: .agents/skills)",
    )
    args = parser.parse_args()

    name = slugify(args.name)
    if not name:
        raise SystemExit("Skill name is empty after normalization.")

    target_dir = Path(args.target_root) / name
    skill_path = target_dir / "SKILL.md"
    if skill_path.exists():
        raise SystemExit(f"Skill already exists: {skill_path}")

    target_dir.mkdir(parents=True, exist_ok=False)
    skill_path.write_text(build_skill_md(name, args.description.strip()), encoding="utf-8")
    print(skill_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
