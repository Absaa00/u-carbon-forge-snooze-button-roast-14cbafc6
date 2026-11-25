#!/usr/bin/env python3
"""Snooze Button Roast — writes one roast line to /output/entry.txt.

Deterministic, no network, no randomness: the same line every run.
"""

import os

ROAST = "My alarm went off at 6 AM on a Saturday like it was clocking in for a shift, so I hit snooze — turns out the snooze button is its union rep."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)

if __name__ == "__main__":
    main()
