"""Funniest One-Line Out-of-Office Reply.

Writes a single out-of-office email auto-reply, one line long, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
"""

import os

LINE = (
    "I've left the office to pursue my dream of not answering emails. "
    "It's going brilliantly \u2014 I'll reply when I wake up."
)


def main() -> None:
    # Gate: the file must be UTF-8 text of 1 to 160 characters, not
    # only whitespace. The entry is the line itself, with no trailing
    # newline, so the file is exactly one line.
    if not 1 <= len(LINE) <= 160 or not LINE.strip():
        raise ValueError("entry line fails the 1-160 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
