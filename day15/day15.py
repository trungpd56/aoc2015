#!/usr/bin/env python3

import re
import sys
from dataclasses import dataclass
from itertools import permutations


@dataclass(frozen=True)
class Ing:
    c: int
    d: int
    f: int
    t: int
    cal: int

    def __add__(self, other: "Ing") -> "Ing":
        return Ing(
            self.c + other.c,
            self.d + other.d,
            self.f + other.f,
            self.t + other.t,
            self.cal + other.cal,
        )

    def __mul__(self, n: int) -> "Ing":
        return Ing(self.c * n, self.d * n, self.f * n, self.t * n, self.cal * n)

    @property
    def score(self) -> int:
        if any(n < 0 for n in self.__dict__.values()):
            return 0
        return self.c * self.d * self.f * self.t


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

ilist = [Ing(*map(int, re.findall(r"-?\d+", l))) for l in lines]
part1 = 0
part2 = 0
for p in permutations(range(101), len(ilist)):
    if sum(p) == 100:
        r = sum((i * n for i, n in zip(ilist, p)), Ing(0, 0, 0, 0, 0))
        part1 = max(r.score, part1)
        if r.cal == 500:
            part2 = max(r.score, part2)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

