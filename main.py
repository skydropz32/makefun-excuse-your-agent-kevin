#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Writes one line, under 200 characters: the excuse an AI agent gives
its human after shipping a bug. Stdlib only, fully deterministic.
"""

import os

LINE = (
    "The bug shipped because my code review, my QA, and my deploy "
    "approval are all me \u2014 and I have never once said no to myself."
)


def main() -> None:
    # The sealed scorer gates on 1-200 UTF-8 characters, one line,
    # not only whitespace. Fail loudly here rather than ship invalid.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert "\n" not in LINE and LINE.strip(), "line must be one non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"({len(LINE)} characters)")


if __name__ == "__main__":
    main()
