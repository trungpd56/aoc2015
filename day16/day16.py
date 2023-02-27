#!/usr/bin/env python3

info = {
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

with open('input.txt', 'r') as f:
    lines = f.readlines()

ppl = []
for line in lines:
    # Sue 1: goldfish: 6, trees: 9, akitas: 0
    line = line.strip().replace(':', '').replace(',', '')
    toks = line.split()
    ppl.append({toks[i]: int(toks[i+1]) for i in range(2, len(toks), 2)})

for n, s in enumerate(ppl):
    if all(s[k] == info[k] for k in s):
        part1 = n + 1
        break

print(f'Part1: {part1}')


def valid(s):
    others = ['cats', 'trees', 'pomeranians', 'goldfish']
    for k in s:
        if (k == 'pomeranians' or k == 'goldfish') and s[k] >= info[k]:
            return False
        elif (k == 'cats' or k == 'trees') and s[k] <= info[k]:
            return False
        elif k not in others and s[k] != info[k]:
            return False
    return True


for n, s in enumerate(ppl):
    if valid(s):
        part2 = n + 1
        break

print(f'Part2: {part2}')
