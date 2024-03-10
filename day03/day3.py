#!/usr/bin/env python3

import sys

dirs = { '>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v':( 1, 0)}

with open(sys.argv[1], 'r') as f:
    line = f.read().strip()

pos = (0, 0)
pos1 = (0, 0)
pos2 = (0, 0)
houses = {pos}
houses2 = {pos}
for i, c in enumerate(line):
    dr, dc = dirs[c]
    pos = (pos[0] + dr, pos[1] + dc)
    if i % 2 == 0:
        pos1 = (pos1[0] + dr, pos1[1] + dc)
        houses2.add(pos1)
    else:
        pos2 = (pos2[0] + dr, pos2[1] + dc)
        houses2.add(pos2)
    houses.add(pos)


part1 = len(houses)
print(f'Part 1: {part1}')
part2 = len(houses2)
print(f'Part 2: {part2}')
