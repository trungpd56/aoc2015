#!/usr/bin/env python3

import sys
import re


with open(sys.argv[1], 'r') as f:
    row, col = map(int, re.findall(r'\d+', f.read()))

num = 20151125
r, c = 1, 1
while True:
    if r == 1:
        r = c + 1
        c = 1
    else:
        r -= 1
        c += 1
    num = (num * 252533) % 33554393
    if r == row and c == col:
        part1 = num
        break

print(f'Part 1: {part1}')

