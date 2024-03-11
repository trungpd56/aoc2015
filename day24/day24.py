#!/usr/bin/env python3

import math
import sys
from itertools import combinations


# this function will not required itertools
# def solve(i: int, cur: tuple, maxlength: int) -> int:
#     if len(cur) > maxlength:
#         return sys.maxsize
#     if sum(cur) == total:
#         return math.prod(cur)
#     if i >= len(nums) or sum(cur) > total:
#         return sys.maxsize
#     r1 = solve(i+1, cur + (nums[i],), maxlength)
#     r2 = solve(i+1, cur, maxlength)
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

