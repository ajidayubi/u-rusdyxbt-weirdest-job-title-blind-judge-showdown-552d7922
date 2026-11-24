#!/usr/bin/env python3
"""Weirdest Job Title entry: writes one job title (<=60 chars) to /output/entry.txt.

The title: a real-sounding job with one gloriously odd twist -- a penguin
counter is a genuine Antarctic research role, and the winter night shift
(the Antarctic winter night lasts months) is the joke.
"""

import os

TITLE = "Lead Penguin Counter, Antarctic Winter Night Shift"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
