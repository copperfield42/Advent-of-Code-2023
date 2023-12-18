# https://adventofcode.com/2023/day/18
from __future__ import annotations
from typing import Iterable
from aoc_utils import test_input, get_raw_data, process_data
import numpy as np
from aoc_recipes import Point, flood_fill


def dig_trench(moves: Iterable[tuple[Point, int]], initial: Point = Point(1, 1)) -> set[Point]:
    digger = initial
    result = {digger}
    x_min, y_min = digger
    for move, n in moves:
        for _ in range(n):
            digger += move
            result.add(digger)
        x_min, y_min = min(x_min, digger.x), min(y_min, digger.y)
    if x_min < initial.x or y_min < initial.y:
        correction = initial - Point(x_min, y_min)
        return {p + correction for p in result}
    return result


def points_to_matrix(points: set[Point]) -> np.ndarray[bool, bool]:
    x, y = float("-inf"), float("-inf")
    for p in points:
        x = max(x, p.x)
        y = max(y, p.y)
    assert x != float("-inf")
    assert y != float("-inf")
    result = np.zeros((x+2, y+2), dtype=bool)
    for p in points:
        result[p] = True
    return result


def main(data: str) -> int:
    """part 1 of the puzzle """
    trench = dig_trench((m, n) for m, n, _ in process_data(data))
    mapa = points_to_matrix(trench)
    fill = flood_fill(mapa)
    return (~fill).sum()


def test() -> bool:
    return main(test_input) == 62


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
