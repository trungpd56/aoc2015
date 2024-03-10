#!/usr/bin/env python3

import sys
from collections import defaultdict

with open(sys.argv[1], "r") as f:
    raws, mole = f.read().strip().split("\n\n")


data = defaultdict(list)
rev = defaultdict(str)
for line in raws.splitlines():
    t = line.split(" => ")
    data[t[0]].append(t[1])
    rev[t[1]] = t[0]

res = set()
for i in range(len(mole)):
    if (k := mole[i]) in data:
        for v in data[k]:
            r = mole[:i] + v + mole[i + 1 :]
            res.add(r)
    if i < len(mole) - 1 and (k := mole[i : i + 2]) in data:
        for v in data[k]:
            r = mole[:i] + v + mole[i + 2 :]
            res.add(r)


part1 = len(res)
print(f"Part 1: {part1}")

part2 = 0
while mole != "e":
    for k, v in rev.items():
        if k in mole:
            mole = mole.replace(k, v, 1)
            part2 += 1

print(f"Part 2: {part2}")

