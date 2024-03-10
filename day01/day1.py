#!/usr/bin/env python3

import sys


with open(sys.argv[1], 'r') as f:
    line = f.read().strip()

part1 = 0
part2 = None
for i, c in enumerate(line, start=1):
    part1 += 1 if c == '(' else -1 #)
    if part1 == -1 and part2 is None:
        part2 = i


print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
