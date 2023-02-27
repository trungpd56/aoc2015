#!/usr/bin/env python3
from collections import defaultdict
from itertools import permutations

with open('input.txt', 'r') as f:
    lines = f.readlines()

dist = defaultdict(int)
locs = set()
for line in lines:
    # London to Dublin = 464
    toks = line.strip().split()
    dist[(toks[0], toks[2])] = int(toks[-1])
    dist[(toks[2], toks[0])] = int(toks[-1])
    locs |= {toks[0], toks[2]}

routes = permutations(locs, len(locs))
distances = []
for r in routes:
    distances.append(sum(dist[(x1, x2)] for x1, x2 in zip(r, r[1:])))

part1 = min(distances)
print(f'Part1: {part1}')

part2 = max(distances)
print(f'Part2: {part2}')
