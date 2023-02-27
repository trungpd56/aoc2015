#!/usr/bin/env python3
import re


def gen(pw):
    code = [ord(c) for c in pw]
    i = len(code)-1
    while True:
        if code[i] == 122:
            code[i] = 97
            i -= 1
            continue
        code[i] += 1
        return ''.join(chr(c) for c in code)


def check(pw):
    if any(c in pw for c in 'iol'):
        return False
    if len(set(re.findall(r'(.)\1', pw))) < 2:
        return False
    code = [ord(c) for c in pw]
    if not any(code[i-1]+1 == code[i] and code[i+1]-1 == code[i]
               for i in range(1, len(code)-1)):
        return False
    return True


with open('input.txt', 'r') as f:
    puzzle = f.read().strip()

first = True
while True:
    puzzle = gen(puzzle)
    if check(puzzle) and first:
        part1 = puzzle
        first = False
    elif check(puzzle):
        part2 = puzzle
        break

print(f'Part1: {part1}')
print(f'Part2: {part2}')
