#!/usr/bin/env python3
from itertools import product
from copy import copy

weapons = [
    {"name": "Dagger", "cost": 8, "damage": 4, "armor": 0},
    {"name": "Shortsword", "cost": 10, "damage": 5, "armor": 0},
    {"name": "Warhammer", "cost": 25, "damage": 6, "armor": 0},
    {"name": "Longsword", "cost": 40, "damage": 7, "armor": 0},
    {"name": "Greataxe", "cost": 74, "damage": 8, "armor": 0}]

armors = [
    {"name": "Leather", "cost": 13, "damage": 0, "armor": 1},
    {"name": "Chainmail", "cost": 31, "damage": 0, "armor": 2},
    {"name": "Splintmail", "cost": 53, "damage": 0, "armor": 3},
    {"name": "Bandedmail", "cost": 75, "damage": 0, "armor": 4},
    {"name": "Platemail", "cost": 102, "damage": 0, "armor": 5}]

rings = [
    {"name": "None", "cost": 0, "damage": 0, "armor": 0},
    {"name": "Damage1", "cost": 25, "damage": 1, "armor": 0},
    {"name": "Damage2", "cost": 50, "damage": 2, "armor": 0},
    {"name": "Damage3", "cost": 100, "damage": 3, "armor": 0},
    {"name": "Defense1", "cost": 20, "damage": 0, "armor": 1},
    {"name": "Defense2", "cost": 40, "damage": 0, "armor": 2},
    {"name": "Defense3", "cost": 80, "damage": 0, "armor": 3}]


class Char():

    def __init__(self, hp, dmg, a, cost):
        self.hp = hp
        self.dmg = dmg
        self.a = a
        self.cost = cost

    def equip(self, w, a, r1, r2):
        return Char(
            self.hp,
            self.dmg + w['damage'] + a['damage'] + r1['damage'] + r2['damage'],
            self.a + w['armor'] + a['armor'] + r1['armor'] + r2['armor'],
            self.cost + w['cost'] + a['cost'] + r1['cost'] + r2['cost'],
        )

    def win(self, other):
        i = 0
        while True:
            if i % 2 == 0:
                other.hp -= max((self.dmg - other.a), 1)
            else:
                self.hp -= max((other.dmg - self.a), 1)
            if other.hp <= 0:
                return True
            elif self.hp <= 0:
                return False
            i += 1


combines = [c for c in product(weapons, armors, rings, rings)
            if c[2]['name'] != c[3]['name'] or c[2]['name'] == 'None']
player = Char(100, 0, 0, 0)
boss = Char(103, 9, 2, 0)

pwin = [player.equip(*c) for c in combines if player.equip(*c).win(copy(boss))]
part1 = min(p.cost for p in pwin)
print(f'Part1: {part1}')

plose = [player.equip(*c) for c in combines if not player.equip(*c).win(copy(boss))]
part2 = max(p.cost for p in plose)
print(f'Part2: {part2}')
