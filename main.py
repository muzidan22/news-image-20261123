#!/usr/bin/env python3
"""Entry for make.fun bounty news-image-20261123.

Sum up the world's news of Monday 23 November 2026 in one image.

The image is held in this repository at assets/entry.png (1024x1024,
181 KB). This program deterministically copies it to the output
directory as entry.png, with no network calls and no randomness.
"""
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "assets" / "entry.png"


def main() -> int:
    if not SOURCE.is_file():
        print(f"missing source image: {SOURCE}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(SOURCE, dest)
    os.chmod(dest, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
