#!/usr/bin/env python3
from collections import defaultdict, namedtuple

with open('input.txt', 'r') as f:
    lines = f.readlines()

reindeer = namedtuple('reindeer', ['v', 't', 'rt'])
info = defaultdict(lambda: reindeer)
for line in lines:
    toks = line.strip().split()
    v, t, rt = map(int, [toks[3], toks[6], toks[-2]])
    info[toks[0]] = reindeer(v, t, rt)

distance = defaultdict(int)
score = defaultdict(int)

for t in range(2503):
    for i in info:
        nt = t % (info[i].t + info[i].rt)
        if nt < info[i].t:
            distance[i] += info[i].v
    lead = max(distance.values())
    for i in info:
        if distance[i] == lead:
            score[i] += 1


part1 = max(distance.values())
print(f'Part1: {part1}')

part2 = max(score.values())
print(f'Part2: {part2}')
