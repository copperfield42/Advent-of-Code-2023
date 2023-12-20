# https://adventofcode.com/2023/day/18
from __future__ import annotations
from aoc_utils import test_input, get_raw_data, process_data, make_polygon


def main(data: str) -> int:
    """part 1 of the puzzle """
    poly = make_polygon((a, b) for a, b, _ in process_data(data))
    return len(poly) + poly.interior_points


def test() -> bool:
    return main(test_input) == 62


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
