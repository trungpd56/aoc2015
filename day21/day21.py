#!/usr/bin/env python3

import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from itertools import product


@dataclass
class Item:
    cost: int
    damage: int
    armor: int


with open("shops.txt", "r") as f:
    raws = f.read().split("\n\n")

items = defaultdict(list)
for i, raw in enumerate(raws):
    for line in raw.splitlines()[1:]:
        items[i].append(Item(*map(int, re.findall(r"\d+", line))))
items[2].append(Item(0, 0, 0))
pairs = list(
    p
    for p in product(items[0], items[1], items[2], items[2])
    if p[2] != p[3] or p[2] == p[3] == (0, 0, 0)
)


class People:
    def __init__(self, line: str) -> None:
        self.hp, self.damage, self.armor = map(int, re.findall(r"\d+", line))
        self.cost = 0

    def __repr__(self) -> str:
        return f"<People {self.__dict__.items()}>"

    def equip(self, items: tuple[Item]):
        for item in items:
            self.armor += item.armor
            self.damage += item.damage
            self.cost += item.cost

    def fight(self, other: "People") -> bool:
        while True:
            other.hp = other.hp - (self.damage - other.armor)
            if other.hp <= 0:
                return True
            self.hp = self.hp - (other.damage - self.armor)
            if self.hp <= 0:
                return False


with open(sys.argv[1], "r") as f:
    line = f.read()

costs = []
lose_costs = []
for p in pairs:
    player = People("100hp, 0 damage, 0 armor")
    boss = People(line)
    player.equip(p)
    if player.fight(boss):
        costs.append(player.cost)
    else:
        lose_costs.append(player.cost)

part1 = min(costs)
print(f"Part 1: {part1}")
part2 = max(lose_costs)
print(f"Part 2: {part2}")

