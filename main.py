#!/usr/bin/env python3
"""Write the one-line excuse entry to the grader output directory.

Stdlib only. Reads the stored line from entry.txt next to this script and
copies it byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import sys


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    if not (1 <= len(text) <= 160) or not text.strip():
        print("entry must be 1-160 non-blank characters", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
