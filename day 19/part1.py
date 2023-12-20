# https://adventofcode.com/2023/day/19
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, flow


def main(data: str) -> int:
    """part 1 of the puzzle """
    workflows, ratings = process_data(data)
    return sum(flow(workflows, r) for r in ratings)


def test() -> bool:
    return main(test_input) == 19114


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
