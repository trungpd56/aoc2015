#!/usr/bin/env python3
from collections import defaultdict


def getnei(G, r, c):
    status = []
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if 0 <= r+dr < maxr and 0 <= c+dc < maxc and not (dr == dc == 0):
                status.append(G[(r+dr, c+dc)])
    return sum(status)


with open('input.txt', 'r') as f:
    lines = f.readlines()

G0 = defaultdict(int)
maxr = len(lines)
maxc = len(lines[0].strip())
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        G0[(r, c)] = 1 if lines[r][c] == '#' else 0


def lights(G, t, part2=False):
    points = [(0, 0), (0, maxc-1), (maxr-1, 0), (maxr-1, maxc-1)]
    if part2:
        for p in points:
            G[p] = 1
    for _ in range(t):
        G1 = defaultdict(int)
        for r in range(maxr):
            for c in range(maxc):
                if part2 and (r, c) in points:
                    G1[(r, c)] = 1
                elif G[(r, c)] == 1:
                    if 2 <= getnei(G, r, c) <= 3:
                        G1[(r, c)] = 1
                    else:
                        G1[(r, c)] = 0
                elif G[(r, c)] == 0:
                    if getnei(G, r, c) == 3:
                        G1[(r, c)] = 1
                    else:
                        G1[(r, c)] = 0
        G = G1
    return sum(G.values())


part1 = lights(G0, 100)
print(f'Part1: {part1}')

part2 = lights(G0, 100, part2=True)
print(f'Part2: {part2}')
