#!/usr/bin/env python3
import json


def solve(x):
    if isinstance(x, int):
        return x
    if isinstance(x, list):
        return sum(solve(i) for i in x)
    if isinstance(x, dict):
        return sum(solve(i) for i in x.values())
    else:
        return 0


def solve2(x):
    if isinstance(x, int):
        return x
    if isinstance(x, list):
        return sum(solve2(i) for i in x)
    if isinstance(x, dict):
        if "red" in x.values():
            return 0
        else:
            return sum(solve2(i) for i in x.values())
    else:
        return 0


with open('input.txt', 'r') as f:
    nums = json.load(f)


part1 = solve(nums)
print(f'Part1: {part1}')

part2 = solve2(nums)
print(f'Part2: {part2}')
