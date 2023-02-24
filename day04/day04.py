#!/usr/bin/env python3
import hashlib

with open('input.txt', 'r') as f:
    data = f.read().strip()

# data = 'abcdef'
i = 0
first = True
while True:
    key = data + str(i)
    hex_hash = hashlib.md5(key.encode()).hexdigest()
    if first and hex_hash.startswith('00000'):
        part1 = i
        first = False
    if hex_hash.startswith('000000'):
        part2 = i
        break
    i += 1


print(f'Part1: {part1}')
print(f'Part2: {part2}')
