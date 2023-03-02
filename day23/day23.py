#!/usr/bin/env python3


class Console():

    def __init__(self, a, lines):
        self.info = [line.strip() for line in lines]
        self.eip = 0
        self.a = a
        self.b = 0

    def run(self):
        while self.eip < len(self.info):
            toks = self.info[self.eip].split()
            if toks[0] == 'hlf':
                self.a /= 2
            elif toks[0] == 'tpl':
                self.a *= 3
            elif toks[0] == 'inc':
                if toks[1] == 'a':
                    self.a += 1
                else:
                    self.b += 1
            elif toks[0] == 'jmp':
                self.eip += int(toks[1])
                continue
            elif toks[0] == 'jie':
                if self.a % 2 == 0:
                    self.eip += int(toks[2])
                    continue
            elif toks[0] == 'jio':
                if self.a == 1:
                    self.eip += int(toks[2])
                    continue
            self.eip += 1
        return self.b


with open('input.txt', 'r') as f:
    lines = f.readlines()

console = Console(0, lines)
part1 = console.run()
print(f'Part1: {part1}')


console2 = Console(1, lines)
part2 = console2.run()
print(f'Part2: {part2}')
