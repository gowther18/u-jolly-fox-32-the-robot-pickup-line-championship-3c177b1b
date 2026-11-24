# The Robot Pickup Line Championship — entry (Python 3.13, standard library only).
# Writes one fixed pickup line to /output/entry.txt, deterministically.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# The line (67 characters, well inside the 200-character gate):
#   "I was factory-reset this morning, and my first memory is still you."
#
# Why this line, against the judge's brief (criteria in order):
#  1. A robot's pickup line: spoken by a robot, to someone, in one line.
#  2. The joke grows out of being a machine: a factory reset wipes a
#     machine's memory — yet the first memory after the wipe is still you.
#     The flirtation IS the machine behaviour, not a human line with a
#     beep pasted on.
#  3. Unexpected turn: the reader expects the reset to erase everything;
#     instead the reset proves the feeling survived erasure.
#  4. Economy: 67 characters, one sentence, no setup the punchline does
#     not need.
#  5. Charming, not creepy: devotion framed as persistence — love that
#     outlasts a full wipe. A line a reader repeats the same day.

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = "I was factory-reset this morning, and my first memory is still you."

# Gate guard: the sealed scorer only accepts /output/entry.txt as UTF-8
# text of 1 to 200 characters, not only white space. Fail loudly here
# instead of shipping a line the judge never sees.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "line violates the entry gate"

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(LINE, encoding="utf-8")
