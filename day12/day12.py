#!/usr/bin/env python3

import json
import sys
from typing import Any


def solve(data: Any, p2: bool = False) -> int:
    if isinstance(data, int):
        return data
    if isinstance(data, list):
        return sum(solve(d, p2) for d in data)
    if isinstance(data, dict):
        if p2 and "red" in data.values():
            return 0
        else:
            return sum(solve(v, p2) for v in data.values())
    return 0


with open(sys.argv[1], "r") as f:
    data = json.load(f)

part1 = solve(data)
print(f"Part 1: {part1}")

part2 = solve(data, True)
print(f"Part 2: {part2}")

