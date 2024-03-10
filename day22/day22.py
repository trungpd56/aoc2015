#!/usr/bin/env python3

import re
import sys
from collections import deque
from copy import deepcopy as cp
from enum import Enum


class Spell(Enum):
    Missile = 1
    Drain = 2
    Shield = 3
    Poison = 4
    Recharge = 5


class Game:
    def __init__(self, line: str, p2: bool) -> None:
        self.hp = 50
        self.mana = 500
        self.manaspent = 0
        self.boss_hp, self.boss_dmg = map(int, re.findall(r"\d+", line))
        self.shield = 0
        self.recharge = 0
        self.poison = 0
        self.armor = 0
        self.p2 = p2

    def __repr__(self) -> str:
        return f"<Game Player({self.hp}hp-{self.mana}mana)-Boss({self.boss_hp}hp-{self.boss_dmg}dmg)({self.p2})>"

    def step(self, spell: Spell):
        if self.p2:
            self.hp -= 1
            if self.hp <= 0:
                return False

        # process effect
        self.armor = 0
        if self.shield > 0:
            self.armor = 7
            self.shield -= 1
        if self.poison > 0:
            self.boss_hp -= 3
            self.poison -= 1
        if self.recharge > 0:
            self.mana += 101
            self.recharge -= 1

        if self.boss_hp <= 0:
            return True

        # equip spell
        mana = 0
        match spell:
            case Spell.Missile:
                mana = 53
                self.boss_hp -= 4
            case Spell.Drain:
                mana = 73
                self.boss_hp -= 2
                self.hp += 2
            case Spell.Shield:
                mana = 113
                self.shield = 6
            case Spell.Poison:
                mana = 173
                self.poison = 6
            case Spell.Recharge:
                mana = 229
                self.recharge = 5
        self.mana -= mana
        self.manaspent += mana

        if self.boss_hp <= 0:
            return True

        # process effect
        self.armor = 0
        if self.shield > 0:
            self.armor += 7
            self.shield -= 1
        if self.poison > 0:
            self.boss_hp -= 3
            self.poison -= 1
        if self.recharge > 0:
            self.mana += 101
            self.recharge -= 1

        if self.boss_hp <= 0:
            return True

        # boss attack:
        if self.boss_dmg > self.armor:
            self.hp -= self.boss_dmg - self.armor
        else:
            self.hp -= 1

        if self.hp <= 0:
            return False


def solve(p2: bool = False):
    queue = deque()
    game = Game(line, p2=p2)
    queue.append((cp(game), Spell.Missile))
    queue.append((cp(game), Spell.Drain))
    queue.append((cp(game), Spell.Shield))
    queue.append((cp(game), Spell.Poison))
    queue.append((cp(game), Spell.Recharge))
    smallest_mana = sys.maxsize

    while queue:
        game, spell = queue.popleft()
        r = game.step(spell)
        match r:
            case False:
                continue
            case True:
                smallest_mana = min(smallest_mana, game.manaspent)
            case None:
                if game.manaspent > smallest_mana:
                    continue
                if game.mana >= 53:
                    queue.append((cp(game), Spell.Missile))
                if game.mana >= 73:
                    queue.append((cp(game), Spell.Drain))
                if game.mana >= 113 and game.shield <= 1:
                    queue.append((cp(game), Spell.Shield))
                if game.mana >= 173 and game.poison <= 1:
                    queue.append((cp(game), Spell.Poison))
                if game.mana >= 229 and game.recharge <= 1:
                    queue.append((cp(game), Spell.Recharge))
    return smallest_mana


with open(sys.argv[1], "r") as f:
    line = f.read()

part1 = solve()
print(f"Part 1: {part1}")

part2 = solve(p2=True)
print(f"Part 2: {part2}")

