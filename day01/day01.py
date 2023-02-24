#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    lines = f.read().strip()

floor = 0
first = True
for i, c in enumerate(lines):
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
    if floor == -1 and first:
        part2 = i+1
        first = False

print(f'Part1: {floor}')
print(f'Part2: {part2}')
