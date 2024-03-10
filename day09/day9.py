#!/usr/bin/env python3

import sys
from collections import defaultdict
from itertools import permutations

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

routes = defaultdict(dict)
for line in lines:
    t = line.split()
    routes[t[0]][t[2]] = int(t[-1])
    routes[t[2]][t[0]] = int(t[-1])

res = []
for p in permutations(routes, len(routes)):
    res.append(sum(routes[x][y] for x, y in zip(p, p[1:])))


part1 = min(res)
print(f"Part 1: {part1}")
part2 = max(res)
print(f"Part 2: {part2}")

