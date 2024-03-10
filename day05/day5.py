#!/usr/bin/env python3

import re
import sys


def valid(line: str) -> bool:
    if (
        sum(line.count(c) for c in "aeiou") >= 3
        and re.search(r"(\w)\1", line)
        and all(p not in line for p in ("ab", "cd", "pq", "xy"))
    ):
        return True
    return False


def valid2(line: str) -> bool:
    if re.search(r"(\w\w)\w*\1", line) and re.search(r"(\w)\w\1", line):
        return True
    return False


with open(sys.argv[1], "r") as f:
    lines = f.readlines()


part1 = sum(valid(l.strip()) for l in lines)
print(f"Part 1: {part1}")

part2 = sum(valid2(l.strip()) for l in lines)
print(f"Part 2: {part2}")

