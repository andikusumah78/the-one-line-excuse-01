#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human — one excuse line.

Pure stdlib Python 3.13, no network, deterministic. The line is 90
characters, inside the 1-160 gate, written to /output/entry.txt.
"""

import os

LINE = (
    "I delegated your deadline to a subagent, and it politely delegated "
    "it straight back to me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
