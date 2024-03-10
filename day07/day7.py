#!/usr/bin/env python3

import sys
from collections import defaultdict
from functools import cache


@cache
def solve(tok: str) -> int:
    if tok.isdigit():
        return int(tok)
    val = data[tok]
    match len(val):
        case 1:
            return solve(val[0])
        case 2:
            return ~solve(val[1]) & 0xFFFF
        case 3:
            v1 = solve(val[0])
            v2 = solve(val[2])
            match val[1]:
                case "AND":
                    return v1 & v2
                case "OR":
                    return v1 | v2
                case "LSHIFT":
                    return v1 << v2
                case "RSHIFT":
                    return v1 >> v2 & 0xFFFF
    # assert False
    return -1


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

data = defaultdict(list)
for line in lines:
    t = line.strip().split(" -> ")
    data[t[1]] = t[0].split()

part1 = solve("a")
print(f"Part 1: {part1}")


data["b"] = [str(part1)]
solve.cache_clear()
part2 = solve("a")
print(f"Part 2: {part2}")

