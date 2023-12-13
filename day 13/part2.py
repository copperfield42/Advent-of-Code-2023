# https://adventofcode.com/2023/day/13
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, find_reflection
import numpy as np
from functools import partial


def is_smudge_reflection[T](img1: np.ndarray[T, T], img2: np.ndarray[T, T]) -> bool:
    return (~(img1 == img2)).sum() == 1


def main(data: str) -> int:
    """part 2 of the puzzle """
    return sum(r.row*100 + r.col for r in map(partial(find_reflection, validator=is_smudge_reflection), process_data(data)))


def test() -> bool:
    return main(test_input) == 400


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
