#!/usr/bin/env python3

import sys
import hashlib


with open(sys.argv[1], 'r') as f:
    line = f.read().strip()

part1 = None
part2 = None
i = 0
while part2 is None:
    res = hashlib.md5(f'{line}{i}'.encode()).hexdigest()
    if res.startswith('00000'):
        if not part1:
            part1 = i
        if res.startswith('000000'):
            part2 = i
    i += 1

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
