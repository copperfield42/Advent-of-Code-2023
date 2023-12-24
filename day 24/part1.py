# https://adventofcode.com/2023/day/24
from __future__ import annotations
from typing import Iterable
from aoc_utils import test_input, get_raw_data, process_data
from aoc_recipes import Point
from dataclasses import dataclass
from functools import cached_property
from itertools_recipes import dotproduct, combinations
import math
from fractions import Fraction
import operator


@dataclass(frozen=True)
class Recta:
    ini: Point
    vector: Point

    @cached_property
    def coeff(self) -> tuple[int, int, int]:
        p1 = self.ini
        p2 = self.ini + self.vector
        d = p1-p2
        a = d.y
        b = -d.x
        c = p1.x * p2.y - p2.x * p1.y
        return a, b, c

    def __call__(self, x, y=None):
        a, b, c = self.coeff
        if y is None:
            if not b:
                raise ValueError("vertical line")
            return (-a*x - c)/b
        if x is None:
            if not a:
                raise ValueError("horizontal line")
            return (-b * y - c) / a
        return a*x + b*y + c

    def find_time(self, value:Point):
        if self(*value) != 0:
            raise ValueError("is not a point of this Line")
        if self.vector.x:
            return Fraction(value.x - self.ini.x, self.vector.x)
        if self.vector.y:
            return Fraction(value.y - self.ini.y, self.vector.y)
        


def are_codirectional[T: Iterable[int]](a: T, b: T) -> bool:
    # https://en.wikipedia.org/wiki/Dot_product
    ma: int = dotproduct(a, a)
    mb: int = dotproduct(b, b)
    ab: int = dotproduct(a, b)
    return Fraction(ab**2, ma*mb) == 1


def find_intersection(r1: Recta, r2: Recta) -> Point | Recta | None:
    if are_codirectional(r1.vector, r2.vector):
        if r1(*r2.ini) == 0:
            return r1
        else:
            return None
    a1, b1, c1 = r1.coeff
    #a2, b2, c2 = r2.coeff
    s1, s2, s3 = map(operator.add, r1.coeff, r2.coeff)
    x = Fraction(s3*b1 - s2*c1, s2*a1 - s1*b1)
    y = r1(x)
    return Point(x, y)


def main(data: str, value_range: tuple[int, int] = (200000000000000, 400000000000000), show: bool=False) -> int:
    """part 1 of the puzzle """
    rectas = [Recta(Point(p.x, p.y), Point(v.x, v.y)) for p, v in process_data(data)]
    # print(rectas)
    # assert all(r(*r.ini) == 0 for r in rectas)
    result = 0
    a, b = value_range
    r1: Recta
    r2: Recta
    for r1, r2 in combinations(rectas, 2):
        inter = find_intersection(r1, r2)
        if show:
            print(f"\n{r1=}\n{r2=}\n{inter=}")
        if inter is None:
            continue
        if isinstance(inter, Recta):
            raise ValueError(f"got a recta {inter}")
        if show:
            print(f"inter={tuple(map(float,inter))}")
        if (a <= inter.x <= b) and (a <= inter.y <= b):
            t1 = r1.find_time(inter)
            t2 = r2.find_time(inter)
            if show:
                print(f"intersect inside at {t1=} {t2=}",)
            result += 1 if t1>=0 and t2>=0 else 0
        else:
            if show:
                print("intersect outside")
        #    raise RuntimeError("invalid state")

    return result


def test() -> bool:
    return main(test_input, (7, 27), True) == 2


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
