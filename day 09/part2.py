# https://adventofcode.com/2023/day/9
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, Sequence, seq_diff


def predictor_back(seq: Sequence[int]) -> int:
    first = [seq[0], *(s[0] for s in seq_diff(seq))]
    result = 0
    for x in reversed(first):
        result = x-result
    return result


def main(data: str) -> int:
    """part 2 of the puzzle """
    return sum(map(predictor_back, process_data(data)))


def test() -> bool:
    return main(test_input) == 2


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
