# https://adventofcode.com/2023/day/10
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, test_input_2, find_max_path


def main(data: str) -> int:
    """part 1 of the puzzle """
    max_path = find_max_path(*process_data(data))
    assert len(max_path)%2==1, "even len max path"
    return len(max_path)//2


def test() -> bool:
    return main(test_input) == 4 and main(test_input_2) == 8


if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
