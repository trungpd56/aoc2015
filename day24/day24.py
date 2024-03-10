#!/usr/bin/env python3

import math
import sys
from functools import cache
from itertools import combinations

# @cache
# def solve(i: int, t: int, qe: tuple) -> tuple[int, int]:
#     if t == total:
#         return len(qe), math.prod(qe)
#     if i >= len(nums) or t > total:
#         return sys.maxsize, sys.maxsize
#     r1 = solve(i+1, t+nums[i], qe+ (nums[i],))
#     r2 = solve(i+1, t, qe)
#     return min(r1, r2)


def solution(l: int):
    even = sum(nums) // l
    for n in range(1, len(nums)):
        groups = [g for g in combinations(nums, n) if sum(g) == even]
        if len(groups) > 0:
            break
    return math.prod(groups[0])


with open(sys.argv[1], "r") as f:
    nums = [int(l) for l in f.readlines()]

# total = sum(nums) // 2

part1 = solution(3)
print(f"Part 1: {part1}")

part2 = solution(4)
print(f"Part 2: {part2}")

