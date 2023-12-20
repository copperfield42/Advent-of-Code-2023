# https://adventofcode.com/2023/day/18
from __future__ import annotations
from typing import Iterable
from aoc_utils import test_input, get_raw_data, MOVES, ir
from aoc_recipes import Point
from dataclasses import dataclass
from collections.abc import Sequence
from fractions import Fraction

N_TO_MOVES = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U",
    }




@dataclass
class Polygon:
    points: Sequence[Point]

    @property
    def area(self) -> int | Fraction:
        # https://en.wikipedia.org/wiki/Shoelace_formula
        points = self.points
        size = len(points)
        a = abs(sum(points[i].x * (points[(i+1)%size].y-points[i-1].y) for i in range(size)))
        if a%2 == 0:
            return a//2
        return Fraction(a, 2)

    def __len__(self) -> int:
        """boundary points"""
        return sum(a.distance_t(b) for a, b in ir.pairwise(self.points))

    @property
    def interior_poins(self) -> int | Fraction:
        # https://en.wikipedia.org/wiki/Pick%27s_theorem
        size = len(self)
        if size % 2 == 0:
            size //= 2
        else:
            size = Fraction(size, 2)
        return self.area + 1 - size


def process_data2(data: str) -> Iterable[tuple[Point, int]]:
    for line in ir.interesting_lines(data):
        _, _, text = line.split()
        text = text[2:-1]
        n = text[:-1]
        yield MOVES[N_TO_MOVES[text[-1]]], int(n, 16)


def make_polygon(data: Iterable[tuple[Point, int]], initial: Point = Point(1, 1)) -> Polygon:
    digger = initial
    result = [initial]
    for move, n in data:
        new = digger + move*n
        result.append(new)
        digger = new
    assert initial == result[-1], "is not a closed poligon"
    return Polygon(result)


def main(data: str):
    """part 2 of the puzzle """
    poly = make_polygon(process_data2(data))
    return len(poly) + poly.interior_poins


def test() -> bool:
    return main(test_input) == 952408144115


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
