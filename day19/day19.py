#!/usr/bin/env python3
from collections import defaultdict

with open('input.txt', 'r') as f:
    data, mol = f.read().strip().split('\n\n')

rep = defaultdict(list)
rev = defaultdict(list)
for line in data.split('\n'):
    toks = line.strip().split(' => ')
    rep[toks[0]].append(toks[1])
    rev[toks[1]] = toks[0]

dist = set()
for i in range(len(mol)):
    for j in range(1, 3):
        if (i+j) <= len(mol) and mol[i:i+j] in rep:
            for k in rep[mol[i:i+j]]:
                newmol = ""
                newmol += mol[:i]
                newmol += k
                newmol += mol[i+j:]
                dist.add(newmol)

part1 = len(dist)
print(f'Part1: {part1}')

rev = sorted(rev.items(), key=lambda x: len(x[0]), reverse=True)
cnt = 0
while True:
    for k, v in rev:
        if k in mol:
            mol = mol.replace(k, v, 1)
            cnt += 1
            break
    if mol == 'e':
        break

part2 = cnt
print(f'Part2: {part2}')
