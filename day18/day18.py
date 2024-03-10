#!/usr/bin/env python3

import sys
from copy import deepcopy
from itertools import product


def display(lines):
    return "\n".join(map("".join, lines))


def cnt(r, c, lines) -> int:
    total = 0
    for dr, dc in product((-1, 0, 1), repeat=2):
        if dr == dc == 0:
            continue
        rr, cc = r + dr, c + dc
        if 0 <= rr < maxr and 0 <= cc < maxc and lines[rr][cc] == "#":
            total += 1
    return total


def game(lines: list[list[str]], p2: bool = False) -> int:
    points = [
        (0, 0),
        (0, maxc - 1),
        (maxr - 1, 0),
        (maxr - 1, maxc - 1),
    ]
    if p2:
        for r, c in points:
            lines[r][c] = '#'
    for _ in range(100):
        nlines = [["#"] * maxc for _ in range(maxr)]
        for r in range(maxr):
            for c in range(maxc):
                if p2 and (r, c) in points:
                    continue
                v, n = lines[r][c], cnt(r, c, lines)
                if v == "#":
                    nlines[r][c] = "#" if n in (2, 3) else "."
                else:
                    nlines[r][c] = "#" if n == 3 else "."
        lines = nlines
    return sum(c == "#" for l in lines for c in l)


with open(sys.argv[1], "r") as f:
    lines = [list(l.strip()) for l in f.readlines()]

maxr = len(lines)
maxc = len(lines[0])

part1 = game(deepcopy(lines))
print(f"Part 1: {part1}")

part2 = game(lines, p2=True)
print(f"Part 2: {part2}")
