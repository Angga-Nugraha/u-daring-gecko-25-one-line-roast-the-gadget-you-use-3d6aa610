"""One-Line Roast entry: writes a single roast line to entry.txt.

Stdlib only — the grader image carries no third-party packages.
"""

import os

TEXT = (
    "One of my wireless earbuds always dies first, so half my life "
    "is mono, like it's 1962."
)


def main() -> None:
    # Self-check against the competition gate: UTF-8 text of 1-200
    # characters, not only white space, on a single line.
    if not 1 <= len(TEXT) <= 200 or not TEXT.strip() or "\n" in TEXT:
        raise SystemExit("roast line fails the 1-200 character single-line gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
