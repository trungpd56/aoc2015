import requests
import os

day = 1
cookies = {"session": "53616c7465645f5f1a87c122dbcf01689453935da09ac400e633263329bccc04933835e6cb41573ea7b25aadc5fefc19e3baa2d004e1aea53cd915ad6727e0d4"}

r = requests.get(
    f'https://adventofcode.com/2015/day/{day}/input', cookies=cookies)

if not os.path.exists(f"day{day:02}"):
    os.mkdir(f"day{day:02}")
os.chdir(f"day{day:02}")

with open('input.txt', 'w') as f:
    f.write(r.text)

sample = f"""\
#!/usr/bin/env python3

import sys

with open('input.txt', 'r') as f:
    lines = f.readlines()


part1 = ""
print(f'Part1: {'{'}part1{'}'}')

part2 = ""
print(f'Part2: {chr(123)}part2{chr(125)}')
"""

if not os.path.isfile(f'day{day:02}.py'):
    with open(f'day{day:02}.py', 'w') as f:
        f.write(sample)
