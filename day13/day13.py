#!/usr/bin/env python3

import sys
from collections import defaultdict
from itertools import permutations


def score(names: set) -> int:
    res = []
    for p in permutations(names, len(names)):
        p = list(p)
        r = sum(data[(x, y)] + data[(y, x)] for x, y in zip(p, p[1:] + [p[0]]))
        res.append(r)
    return max(res)


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

data = defaultdict(int)
names = set()
for l in lines:
    t = l.strip("\n.").split()
    val = int(t[3]) if t[2] == "gain" else -int(t[3])
    data[(t[0], t[-1])] = val
    names.update((t[0], t[-1]))


part1 = score(names)
print(f"Part 1: {part1}")

names.add("Trung")
part2 = score(names)
print(f"Part 2: {part2}")

