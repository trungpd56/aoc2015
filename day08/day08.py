#!/usr/bin/env python3
import re

with open('input.txt', 'r') as f:
    lines = f.readlines()

code, memory = 0, 0
for line in lines:
    raw = line.strip()
    memory += len(raw)
    string = re.sub(r'\\x[a-f0-9]{2}', 'x', raw)
    string = re.sub(r'\\\\', 'x', string)
    string = re.sub(r'\\"', 'x', string)
    code += len(string) - 2

part1 = memory - code
print(f'Part1: {part1}')

encode = 0
for line in lines:
    raw = line.strip()
    string = re.sub(r'\\', 'xx', raw)
    string = re.sub(r'"', 'yy', string)
    encode += len(string) + 2
part2 = encode - memory
print(f'Part2: {part2}')
