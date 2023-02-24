#!/usr/bin/env python3

moves = {'>': (1, 0), '<': (-1, 0), '^': (0, 1), 'v': (0, -1)}

with open('input.txt', 'r') as f:
    data = f.read().strip()

pos = (0, 0)
houses = {(0, 0)}
santa, robo = (0, 0), (0, 0)
houses2 = {(0, 0)}
for i, c in enumerate(data):
    x, y = moves[c]
    pos = (pos[0]+x, pos[1] + y)
    houses.add(pos)
    if i % 2:
        robo = (robo[0]+x, robo[1]+y)
        houses2.add(robo)
    else:
        santa = (santa[0]+x, santa[1]+y)
        houses2.add(santa)

part1 = len(houses)
print(f'Part1: {part1}')

part2 = len(houses2)
print(f'Part2: {part2}')
