#!/usr/bin/env python3
"""Writes one office-life joke line to /output/entry.txt deterministically."""
import os

LINE = "I typed 'per my last email' once and now HR treats my keyboard like a loaded weapon."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
