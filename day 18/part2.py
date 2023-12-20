# https://adventofcode.com/2023/day/18
from __future__ import annotations
from typing import Iterable
from aoc_utils import test_input, get_raw_data, MOVES, make_polygon, ir
from aoc_recipes import Point


N_TO_MOVES = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U",
    }


def process_data2(data: str) -> Iterable[tuple[Point, int]]:
    for line in ir.interesting_lines(data):
        _, _, text = line.split()
        text = text[2:-1]
        n = text[:-1]
        yield MOVES[N_TO_MOVES[text[-1]]], int(n, 16)


def main(data: str):
    """part 2 of the puzzle """
    poly = make_polygon(process_data2(data))
    return len(poly) + poly.interior_points


def test() -> bool:
    return main(test_input) == 952408144115


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
