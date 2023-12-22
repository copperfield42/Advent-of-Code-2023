# https://adventofcode.com/2023/day/22
from __future__ import annotations

from typing import Iterator, Iterable, Self
import itertools_recipes as ir
from ast import literal_eval
from aoc_recipes import Point3
from dataclasses import dataclass
from functools import cached_property, cache


test_input = """
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
"""

@dataclass(eq=True, frozen=True)
class Brick:
    ini: Point3
    fin: Point3

    @cached_property
    def high(self) -> tuple[int, int]:
        a, b = sorted([self.ini.z, self.fin.z])
        return a, b

    @cached_property
    def vector(self) -> Point3:
        return (self.fin - self.ini).normalize()

    def __post_init__(self):
        assert sum(x1 == x2 for x1, x2 in zip(self.ini, self.fin)) >= 2, "invalid brick"

    def __iter__(self):
        move = self.vector
        fin = self.fin
        p = self.ini
        while p != fin:
            yield p
            p += move
        yield fin

    def __len__(self):
        move = self.fin - self.ini
        return next((abs(n) for n in move if n), 0) + 1

    def __contains__(self, item):
        if not isinstance(item, Point3):
            return False
        for vi, ii, s1, s2 in zip(self.vector, item, self.ini, self.fin):
            if vi == 0:
                if ii != s1:
                    return False
            else:
                if not (s1 <= ii <= s2 or s2 <= ii <= s1):
                    return False
        return True

    def move_vertically(self, z: int) -> Self:
        move = Point3(0, 0, z)
        return type(self)(self.ini + move, self.fin + move)

    def collide(self, other: Brick) -> bool:
        a, b = self.high
        c, d = other.high
        if c <= a <= d or c <= b <= d:
            return any(x in other for x in self)
        return False


def process_data(data: str) -> Iterable[Brick]:
    """transform the raw data into a processable form"""
    for line in ir.interesting_lines(data):
        a, b = line.split("~")
        yield Brick(Point3(*literal_eval(a)), Point3(*literal_eval(b)))
    pass


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
