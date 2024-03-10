#!/usr/bin/env python3

import sys

def cal(x,y,z, p2: bool=False) -> int:
    x, y, z = sorted((x, y, z))
    if not p2:
        return 2*x*y + 2*y*z + 2*z*x + x*y
    return x*y*z + 2*(x+y)


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

part1 = 0
part2 = 0
for line in lines:
    x, y, z = map(int, line.split('x'))
    part1 += cal(x, y, z)
    part2 += cal(x, y, z, p2=True)

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
