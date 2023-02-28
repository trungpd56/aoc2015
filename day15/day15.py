#!/usr/bin/env python3
import re
from collections import Counter
from itertools import combinations_with_replacement


class Ingredient():

    def __init__(self, c, d, f, t, cal):
        self.capacity = c
        self.durability = d
        self.flavor = f
        self.texture = t
        self.calories = cal

    def __add__(self, others):
        return Ingredient(
            self.capacity + others.capacity,
            self.durability + others.durability,
            self.flavor + others.flavor,
            self.texture + others.texture,
            self.calories + others.calories
        )

    def __mul__(self, x):
        return Ingredient(
            self.capacity * x,
            self.durability * x,
            self.flavor * x,
            self.texture * x,
            self.calories * x
        )

    def score(self):
        if self.capacity < 0 or self.durability < 0 or self.flavor < 0\
           or self.texture < 0:
            return 0
        return self.capacity * self.durability * self.flavor * self.texture


with open('input.txt', 'r') as f:
    lines = f.readlines()

info = {}
for line in lines:
    name = line.split()[0].strip(':')
    info[name] = Ingredient(*map(int, re.findall(r'-?\d+', line)))

cookies = []
recipes = [Counter(i) for i in combinations_with_replacement(info, 100)]
for r in recipes:
    cookie = Ingredient(0, 0, 0, 0, 0)
    for i, n in r.items():
        cookie += info[i] * n
    cookies.append(cookie)

part1 = max(cookie.score() for cookie in cookies)
print(f'Part1: {part1}')

part2 = max([cookie.score() for cookie in cookies if cookie.calories == 500])
print(f'Part2: {part2}')
