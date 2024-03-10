#!/usr/bin/env python3

import re
import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

deers = []
for line in lines:
    deers.append(tuple(map(int, re.findall(r"\d+", line))))

res = [0] * len(deers)
score = [0] * len(deers)
for t in range(2503):
    for i, (v, vt, rt) in enumerate(deers):
        tt = t % (vt + rt)
        if tt < vt:
            res[i] += v
    maxd = max(res)
    for i in range(len(res)):
        if res[i] == maxd:
            score[i] += 1


part1 = max(res)
print(f"Part 1: {part1}")
part2 = max(score)
print(f"Part 2: {part2}")

