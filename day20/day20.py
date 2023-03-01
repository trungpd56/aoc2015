#!/usr/bin/env python3
from collections import defaultdict

with open('input.txt', 'r') as f:
    presents = int(f.read())

num_elfs = presents // 10
houses = defaultdict(int)
for elf_id in range(1, num_elfs+1):
    loc = elf_id
    while loc < num_elfs:
        houses[loc] += elf_id * 10
        loc += elf_id

for id in houses:
    if houses[id] >= presents:
        part1 = id
        break

print(f'Part1: {part1}')

num_elfs = presents // 11
houses2 = defaultdict(int)
for elf_id in range(1, num_elfs+1):
    loc = elf_id
    delivered = 0
    while loc < num_elfs and delivered < 50:
        houses2[loc] += elf_id * 11
        loc += elf_id
        delivered += 1

for id in houses2:
    if houses2[id] >= presents:
        part2 = id
        break

print(f'Part2: {part2}')
