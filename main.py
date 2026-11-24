#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one line, in the dog's own voice, to /output/entry.txt.
Python 3.13 standard library only; deterministic output.
"""

import os

ENTRY = (
    "Your homework smelled like bacon because you did it next to the "
    "pizza box, and I am a dog with zero impulse control and a law "
    "degree in snacks. Honestly? It never stood a chance."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200) or "\n" in text:
        raise ValueError("entry must be one line of 1-200 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
