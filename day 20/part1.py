# https://adventofcode.com/2023/day/20
from __future__ import annotations
from aoc_utils import test_input, get_raw_data, process_data, test_input_2
from aoc_recipes import Point


def main(data: str) -> int:
    """part 1 of the puzzle """
    machine = process_data(data)
    total = sum((machine() for _ in range(1000)), start=Point(0, 0))
    print(total)
    return total.x * total.y


def test() -> bool:
    return main(test_input) == 32000000 and main(test_input_2) == 11687500


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
