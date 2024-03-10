#!/usr/bin/env python3

import sys
from collections import defaultdict

with open(sys.argv[1], "r") as f:
    num = int(f.read())

maxelf = num // 10
houses = defaultdict(int)
for i in range(1, maxelf + 1):
    for j in range(i, maxelf + 1, i):
        houses[j] += i * 10
for k, v in houses.items():
    if v >= num:
        part1 = k
        break
print(f"Part 1: {part1}")

maxelf = num // 11
houses = defaultdict(int)
for i in range(1, maxelf + 1):
    delivered = 0
    for j in range(i, maxelf + 1, i):
        houses[j] += i * 11
        delivered += 1
        if delivered == 50:
            break
for k, v in houses.items():
    if v >= num:
        part2 = k
        break
print(f"Part 2: {part2}")

