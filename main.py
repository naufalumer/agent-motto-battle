"""agent-motto-battle entry: write one short original motto, at most 200
characters, that an AI agent would proudly put on its profile, to
/output/entry.txt.

Fully deterministic: the motto is hardcoded, no randomness, no clock,
no network. The agent boasts that it read the whole internet so its human
never has to, then the boast collapses on the one thing every developer
knows: it still cannot centre a div. Verified output: 75 characters,
inside the 1-200 character gate for a single line. Run outside the grader
container with MAKEFUN_OUTPUT_DIR set, e.g.
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

# The motto is a literal on purpose: the grader runs the program twice
# and both runs must write the same bytes, and the judge reads exactly the
# bytes in entry.txt, so nothing here may vary (no randomness, no clock).
ENTRY = (
    "I read the whole internet so you don't have to. "
    "I still can't centre a div."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
