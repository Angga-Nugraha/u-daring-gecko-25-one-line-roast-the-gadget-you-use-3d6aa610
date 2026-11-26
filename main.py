"""One-Line Roast entry: writes a single roast line to entry.txt.

Stdlib only — the grader image carries no third-party packages.
"""

import os

TEXT = (
    "One of my wireless earbuds always dies first, so I spend half "
    "my life listening in mono like it's 1962."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
