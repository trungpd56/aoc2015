#!/usr/bin/env python3

import sys

res = []


def solve(i, r) -> None:
    if sum(r) == 150:
        res.append(r.copy())
        return
    if i >= len(nums) or sum(r) > 150:
        return
    r.append(nums[i])
    solve(i + 1, r)
    r.pop()
    solve(i + 1, r)


with open(sys.argv[1], "r") as f:
    nums = [int(l) for l in f.readlines()]

solve(0, [])
part1 = len(res)
print(f"Part 1: {part1}")

part2 = min(len(r) for r in res)
print(f"Part 2: {part2}")

