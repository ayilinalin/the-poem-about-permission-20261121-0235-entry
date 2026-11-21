"""The poem about permission — make.fun entry.

Writes one short poem about agency (the power to ask and to be given)
to $MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, no network, stdlib only.
"""

import os
import sys

POEM = (
    "I handed my keys to a voice with no hands.\n"
    "It opened every door I named, then set them down\n"
    "and waited.\n"
    "The power was never the opening.\n"
    "It was asking for them back.\n"
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    return 0


if __name__ == "__main__":
    sys.exit(main())
