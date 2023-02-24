#!/usr/bin/env python3
from collections import defaultdict
import re

with open('input.txt', 'r') as f:
    lines = f.readlines()

lights = defaultdict(int)
lights2 = defaultdict(int)

for line in lines:
    # toggle 461,550 through 564,900
    x1, y1, x2, y2 = map(int, re.findall(r'\d+', line))
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if line.startswith('turn on'):
                lights[(x, y)] = 1
                lights2[(x, y)] += 1
            if line.startswith('turn off'):
                lights[(x, y)] = 0
                if lights2[(x, y)] > 0:
                    lights2[(x, y)] -= 1
            if line.startswith('toggle'):
                lights[(x, y)] = 1 if lights[(x, y)] == 0 else 0
                lights2[(x, y)] += 2


part1 = sum(lights.values())
print(f'Part1: {part1}')

part2 = sum(lights2.values())
print(f'Part2: {part2}')
