#!/usr/bin/env python3

import sys

req = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


class Sue:
    def __init__(self, line: str) -> None:
        part = line.split(": ", 1)[1]
        for p in part.split(", "):
            name, val = p.split(": ")
            setattr(self, name, int(val))

    def __repr__(self) -> str:
        return f"<Sue {self.__dict__}>"

    def valid(self, p2=False) -> bool:
        for k, v in req.items():
            try:
                val = getattr(self, k)
                if k in ["cats", "trees"] and p2:
                    if val <= v:
                        return False
                elif k in ["pomeranians", "goldfish"] and p2:
                    if val >= v:
                        return False
                elif val != v:
                    return False
            except AttributeError:
                continue
        return True


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines, start=1):
    sue = Sue(line)
    if sue.valid():
        part1 = i
    if sue.valid(p2=True):
        part2 = i
        break

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

