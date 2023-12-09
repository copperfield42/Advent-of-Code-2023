# https://adventofcode.com/2023/day/9
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, seq_diff, Sequence


def predictor(seq: Sequence[int]) -> int:
    last = [seq[-1], *(s[-1] for s in seq_diff(seq))]
    return sum(last)


def main(data: str) -> int:
    """part 1 of the puzzle """
    return sum(map(predictor, process_data(data)))


def test() -> bool:
    return main(test_input) == 114


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
