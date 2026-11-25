"""Charm the Commuter: forecast for Updraft Falls, a city that isn't.

The line is a one-line broadcast forecast for an invented city where
snow falls upwards. It keeps the rhythm of real weather reporting,
gives the city one concrete detail (flakes land on rooftops first),
and hands the bored commuter a small, hopeful image on the stairs.
"""

import os

LINE = (
    "Updraft Falls: snow falling up, 3°C, flakes landing on "
    "rooftops first — catch one on the stairs, the 7:40 leaves "
    "on time, sky permitting."
)


MAX_CHARS = 140


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(f"line is {len(LINE)} chars, must be 1-{MAX_CHARS}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(LINE.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
