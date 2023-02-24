#!/usr/bin/env python3
from functools import cache


@cache
def solve(x):
    try:
        return int(x)
    except:
        pass
    toks = signal[x]
    if len(toks) == 1:
        return solve(toks[0])
    elif len(toks) == 2:
        return ~ solve(toks[1]) & 65535
    else:
        if toks[1] == 'AND':
            return solve(toks[0]) & solve(toks[2])
        if toks[1] == 'OR':
            return solve(toks[0]) | solve(toks[2])
        if toks[1] == 'LSHIFT':
            return solve(toks[0]) << solve(toks[2])
        if toks[1] == 'RSHIFT':
            return solve(toks[0]) >> solve(toks[2]) & 65535


with open('input.txt', 'r') as f:
    lines = f.readlines()


signal = {}
for line in lines:
    toks = line.strip().split(' -> ')
    signal[toks[1]] = toks[0].split()


part1 = solve('a')
print(f'Part1: {part1}')


solve.cache_clear()
signal['b'] = [part1]
part2 = solve('a')
print(f'Part2: {part2}')
