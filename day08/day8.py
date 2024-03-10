#!/usr/bin/env python3

import re
import sys

with open(sys.argv[1], "r") as f:
    lines = [l.strip() for l in f.readlines()]

code, mem = 0, 0
encode = 0
for line in lines:
    code += len(line)
    encode += len(line) + 2 + line.count('"') + line.count("\\")
    line = re.sub(r'\\"', '"', line)
    line = re.sub(r"\\x[a-f0-9]{2}", "x", line)
    line = re.sub(r"\\\\", r"\\", line)
    mem += len(line) - 2


part1 = code - mem
print(f"Part 1: {part1}")

part2 = encode - code
print(f"Part 2: {part2}")

