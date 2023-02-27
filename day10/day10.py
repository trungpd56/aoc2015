#!/usr/bin/env python3
from itertools import groupby


def lookandsay(s):
    return ''.join([str(len(list(g)))+k for k, g in groupby(s)])


with open('input.txt', 'r') as f:
    data = f.read().strip()

for t in range(50):
    data = lookandsay(data)
    if t+1 == 40:
        part1 = len(data)

print(f'Part1: {part1}')
print(f'Part2: {len(data)}')
