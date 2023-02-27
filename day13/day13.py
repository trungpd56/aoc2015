#!/usr/bin/env python3
from collections import defaultdict
from itertools import permutations

with open('input.txt', 'r') as f:
    lines = f.readlines()

info = defaultdict(int)
persons = set()
for line in lines:
    toks = line.strip('.\n').split()
    if toks[2] == 'gain':
        info[(toks[0], toks[-1])] = int(toks[3])
    if toks[2] == 'lose':
        info[(toks[0], toks[-1])] = -int(toks[3])
    persons |= {toks[0], toks[-1]}

tables = permutations(persons, len(persons))
total = []
for t in tables:
    h = sum(info[x1, x2] + info[x2, x1] for x1, x2 in zip(t, t[1:]+(t[0],)))
    total.append(h)

part1 = max(total)
print(f'Part1: {part1}')

persons.add('Trung')
tables = permutations(persons, len(persons))
total = []
for t in tables:
    h = sum(info[x1, x2] + info[x2, x1] for x1, x2 in zip(t, t[1:]+(t[0],)))
    total.append(h)

part2 = max(total)
print(f'Part2: {part2}')
