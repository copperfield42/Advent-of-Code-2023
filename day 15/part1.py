# https://adventofcode.com/2023/day/15
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, lens_hash


def main(data: str) -> int:
    """part 1 of the puzzle """
    return sum(map(lens_hash, process_data(data)))


def test() -> bool:
    return main(test_input) == 1320


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
