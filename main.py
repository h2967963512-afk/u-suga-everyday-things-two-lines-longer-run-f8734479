"""Writes the two-line entry to /output/entry.txt.

Line 1 explains a traffic jam to a 10-year-old in one vivid sentence,
built on a single analogy: a whole road of cars drinking through one
tiny straw. Line 2 says in one sentence what that analogy maps (the
road narrowing slows everything to a trickle) and what it leaves out
(the drivers, who can honk, change lanes, and pick another road).

Python 3.13, standard library only, no network.

How it runs: `python3 main.py` creates /output if needed and writes the
two lines to /output/entry.txt with no trailing newline. Verification:
run it and check /output/entry.txt is UTF-8, exactly 2 lines, 264
characters total (line 1: 94, line 2: 169), inside the gate's 1-400
character window. Re-running after a docstring-only edit must leave
the output byte-identical (sha256 f77778a01e4957d1d37b69be1f6700197691a0f49a66df62d3ddbb52f929a4d4).
"""

import os

LINE_1 = "A traffic jam is a whole road of cars trying to drink through one tiny straw at the same time."
LINE_2 = "The straw shows why everything slows to a trickle when the road narrows, but it leaves out the drivers, who can honk, change lanes, and choose a different road entirely."

TEXT = LINE_1 + "\n" + LINE_2


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
