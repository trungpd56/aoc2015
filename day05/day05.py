#!/usr/bin/env python3
import re


def nice(s):
    if sum(1 for c in s if c in 'aeiou') < 3:
        return False
    if not re.search(r'(.)\1', s):
        return False
    if any(i in s for i in ('ab', 'cd', 'pq', 'xy')):
        return False
    return True


def nice2(s):
    if not re.search(r'(.).\1', s):
        return False
    if not re.search(r'(..).*\1', s):
        return False
    return True


with open('input.txt', 'r') as f:
    lines = f.readlines()

part1 = sum(nice(line) for line in lines)
print(f'Part1: {part1}')

part2 = sum(nice2(line) for line in lines)
print(f'Part2: {part2}')
