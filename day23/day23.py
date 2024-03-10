#!/usr/bin/env python3

import sys


class Computer:
    def __init__(self, lines: list[str], a: int = 0) -> None:
        self.regs = {}
        self.regs["a"] = a
        self.regs["b"] = 0
        self.lines = [l.strip() for l in lines]

    def run(self):
        eip = 0
        while eip < len(self.lines):
            t = self.lines[eip].split()
            match t[0]:
                case "hlf":
                    self.regs[t[1]] //= 2
                    eip += 1
                case "tpl":
                    self.regs[t[1]] *= 3
                    eip += 1
                case "inc":
                    self.regs[t[1]] += 1
                    eip += 1
                case "jmp":
                    eip += int(t[1])
                case "jie":
                    eip += int(t[2]) if self.regs[t[1].strip(",")] % 2 == 0 else 1
                case "jio":
                    eip += int(t[2]) if self.regs[t[1].strip(",")] == 1 else 1
        return self.regs["b"]


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

comp = Computer(lines)
part1 = comp.run()
print(f"Part 1: {part1}")


comp = Computer(lines, a=1)
part2 = comp.run()
print(f"Part 2: {part2}")

