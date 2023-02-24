#!/usr/bin/env python3


def paper(x, y, z):
    return 2*x*y + 2*y*z + 2*z*x + x*y


def ribbon(x, y, z):
    return x*y*z + 2*x + 2*y


with open('input.txt', 'r') as f:
    boxes = [sorted(int(x) for x in line.split('x')) for line in f.readlines()]


part1 = sum(paper(*box) for box in boxes)
print(f'Part1: {part1}')

part2 = sum(ribbon(*box) for box in boxes)
print(f'Part2: {part2}')
