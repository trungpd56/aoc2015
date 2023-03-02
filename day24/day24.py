#!/usr/bin/env python3
from itertools import combinations
from math import prod

with open('input.txt', 'r') as f:
    nums = [int(line) for line in f.readlines()]

i = 1
while True:
    comb = [comb for comb in combinations(nums, i) if sum(comb) == 516]
    if len(comb) > 0:
        break
    i += 1

part1 = min(prod(c) for c in comb)
print(f'Part1: {part1}')

i = 1
while True:
    comb2 = [comb for comb in combinations(nums, i) if sum(comb) == 387]
    if len(comb2) > 0:
        break
    i += 1

part2 = min(prod(c) for c in comb2)
print(f'Part2: {part2}')
