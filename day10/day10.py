#!/usr/bin/env python3

import sys


def gen(line: str) -> str:
    res = ""
    cur = line[0]
    cnt = 0
    for c in line:
        if c == cur:
            cnt += 1
        else:
            res += f"{cnt}{cur}"
            cur = c
            cnt = 1
    return res + f"{cnt}{cur}"


with open(sys.argv[1], "r") as f:
    line = f.read().strip()

part1 = 0
for t in range(50):
    line = gen(line)
    if t == 39:
        part1 = len(line)
print(f"Part 1: {part1}")
part2 = len(line)
print(f"Part 2: {part2}")

