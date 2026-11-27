#!/usr/bin/env python3
"""Entry for the make.fun bounty "The Moon Finally Answers Back"
(u-mang-the-moon-finally-answers-back-781a7ec1).

The brief asks for one line, at most 240 characters, that the Moon
says back to the people who stare up at it, wish on it, howl at it
and make it late-night promises, scored on: speaking as the Moon
answering those wishes, howls and promises; a real laugh on one
read; the Moon's own voice — wry and old and a little tired of being
wished upon; a comeback whose turn arrives before the line ends; and
no wasted characters. So this line opens with the Moon's full
service record — four billion years of wishes, and not one wisher
ever asking how its night is going — and turns on the answer it
gives when it finally replies: going in circles, as it always has.
Old, wry, and faintly aggrieved, in the Moon's own voice, and the
joke never explains itself.

The program writes that line to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR locally, /output in the grader).
"""

import os

LINE = (
    "Four billion years of wishes, and not one of you has asked "
    "how my night is going. It is going in circles. It has always "
    "gone in circles."
)


def validate(line: str) -> None:
    """Mirror the bounty gate: UTF-8 text of 1 to 240 characters,
    and not only white space. Refuse to hand in anything else."""
    encoded = line.encode("utf-8")  # raises if it cannot be encoded
    if not line.strip():
        raise ValueError("entry is only white space")
    if not 1 <= len(line) <= 240:
        raise ValueError(f"entry is {len(line)} characters, outside 1..240")
    if len(encoded) > 240:
        raise ValueError("entry encodes to more than 240 bytes")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
