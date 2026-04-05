#!/usr/bin/env python3
"""Extract text from a local PDF file using pdftotext."""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract text from a PDF with pdftotext.")
    parser.add_argument("pdf_path", help="Path to the local PDF file")
    parser.add_argument("--output-path", help="Path to output .txt file")
    args = parser.parse_args()

    if shutil.which("pdftotext") is None:
        raise SystemExit("pdftotext is not installed.")

    pdf_path = Path(args.pdf_path)
    if not pdf_path.exists():
        raise SystemExit(f"File does not exist: {pdf_path}")

    if args.output_path:
        output_path = Path(args.output_path)
    else:
        output_dir = Path("drafts/demo/extracted")
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f"{pdf_path.stem}.txt"

    subprocess.run(["pdftotext", str(pdf_path), str(output_path)], check=True)
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
