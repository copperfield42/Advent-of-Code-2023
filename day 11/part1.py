# https://adventofcode.com/2023/day/11
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, Iterable
from aoc_recipes import Point, where2
import itertools


def expand_galaxies(data: Iterable[Point], shiftx: set[int], shifty: set[int], expansion_factor: int = 1) -> Iterable[Point]:
    for p in data:
        x, y = p
        dx = sum(sx < x for sx in shiftx) * expansion_factor
        dy = sum(sy < y for sy in shifty) * expansion_factor
        yield p + (dx, dy)


def main(data: str, expansion_factor: int = 1) -> int:
    """part 1 of the puzzle """
    img = process_data(data)
    x, y = img.shape
    galaxies = frozenset(where2(img))
    shiftx = set(range(x)) - {g.x for g in galaxies}
    shifty = set(range(y)) - {g.y for g in galaxies}
    exp_galaxies = frozenset(expand_galaxies(galaxies, shiftx, shifty, expansion_factor))
    return sum(g1.distance_t(g2) for g1, g2 in itertools.combinations(exp_galaxies, 2))


def test() -> bool:
    return main(test_input) == 374


if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
