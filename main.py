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
    # The gate accepts UTF-8 text of 1 to 160 characters, not only
    # whitespace; fail loudly here rather than shipping a bad entry.
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
