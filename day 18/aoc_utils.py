# https://adventofcode.com/2023/day/18
from __future__ import annotations
from typing import Iterable, Sequence
import itertools_recipes as ir
from aoc_recipes import DIRECCIONES, Point
from dataclasses import dataclass
from fractions import Fraction

MOVES = {
    "U": DIRECCIONES["^"],
    "D": DIRECCIONES["v"],
    "L": DIRECCIONES["<"],
    "R": DIRECCIONES[">"],
    }


test_input = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""


@dataclass
class Polygon:
    points: Sequence[Point]

    @property
    def area(self) -> int | Fraction:
        # https://en.wikipedia.org/wiki/Shoelace_formula
        points = self.points
        size = len(points)
        a = abs(sum(points[i].x * (points[(i+1) % size].y-points[i-1].y) for i in range(size)))
        if a % 2 == 0:
            return a//2
        return Fraction(a, 2)

    def __len__(self) -> int:
        """boundary points"""
        return sum(a.distance_t(b) for a, b in ir.pairwise(self.points))

    @property
    def interior_points(self) -> int | Fraction:
        # https://en.wikipedia.org/wiki/Pick%27s_theorem
        size = len(self)
        if size % 2 == 0:
            size //= 2
        else:
            size = Fraction(size, 2)
        return self.area + 1 - size


def make_polygon(data: Iterable[tuple[Point, int]], initial: Point = Point(0, 0)) -> Polygon:
    digger = initial
    result = [initial]
    for move, n in data:
        new = digger + move * n
        result.append(new)
        digger = new
    assert initial == result[-1], "is not a closed polygon"
    return Polygon(result)


def process_data(data: str) -> Iterable[tuple[Point, int, str]]:
    """transform the raw data into a processable form"""
    for line in ir.interesting_lines(data):
        move, n, rgb = line.split()
        yield MOVES[move], int(n), rgb[2:-1]


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
