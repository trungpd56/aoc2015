#!/usr/bin/env python3

import re
import sys
from collections import defaultdict

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

lights = defaultdict(lambda: False)
lights2 = defaultdict(int)
for line in lines:
    x1, y1, x2, y2 = map(int, re.findall(r"\d+", line))
    if line.startswith("toggle"):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                lights[(x, y)] = not lights[(x, y)]
                lights2[(x, y)] += 2
    elif line.startswith("turn off"):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                lights[(x, y)] = False
                lights2[(x, y)] = max(0, lights2[(x, y)] - 1)
    elif line.startswith("turn on"):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                lights[(x, y)] = True
                lights2[(x, y)] += 1
    else:
        assert False

part1 = sum(lights.values())
print(f"Part 1: {part1}")
part2 = sum(lights2.values())
print(f"Part 2: {part2}")

