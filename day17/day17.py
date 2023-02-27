#!/usr/bin/env python3
from itertools import combinations

with open('input.txt', 'r') as f:
    containers = [int(line) for line in f.readlines()]

ways = []
for n in range(1, len(containers)+1):
    ways.extend([i for i in combinations(containers, n) if sum(i) == 150])

part1 = len(ways)
print(f'Part1: {part1}')

minimum = min(len(w) for w in ways)
print(f'Part2: {len([w for w in ways if len(w) == minimum])}')
