#!/usr/bin/env python3

import re
import sys
from string import ascii_lowercase as lc
from typing import Iterator


def valid(line: str) -> bool:
    c1 = any("".join(g) in line for g in zip(lc, lc[1:], lc[2:]))
    c2 = all(c not in line for c in "iol")
    c3 = re.findall(r"(\w)\1", line)
    return c1 and c2 and (len(c3) >= 2)


def gen(line: str) -> Iterator[str]:
    nums = [ord(c) for c in line]
    minc = ord("a")
    maxc = ord("z")
    i = len(line) - 1
    while True:
        nums[i] += 1
        if nums[i] > maxc:
            nums[i] = minc
            while i - 1 >= 0 and nums[i - 1] == maxc:
                nums[i - 1] = minc
                i -= 1
            nums[i - 1] += 1
            i = len(line) - 1
        yield "".join(map(chr, nums))


with open(sys.argv[1], "r") as f:
    line = f.read().strip()

g = gen(line)
part1 = None
while True:
    pw = next(g)
    print(f"\rPassword: {pw:10s}", end="")
    if valid(pw):
        if part1 is None:
            part1 = pw
        else:
            print()
            break

print(f"Part 1: {part1}")
part2 = pw
print(f"Part 2: {part2}")

