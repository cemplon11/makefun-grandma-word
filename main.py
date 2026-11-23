#!/usr/bin/env python3
"""One Word From Grandma (make.fun).

Writes exactly one word — the single word grandma would text about AI —
to /output/entry.txt. Pure Python stdlib, deterministic, no network.
"""

import os

WORD = "witchcraft"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
