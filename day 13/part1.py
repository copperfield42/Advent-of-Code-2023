# https://adventofcode.com/2023/day/13
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, find_reflection
import numpy as np
from functools import partial


def is_reflection[T](img1: np.ndarray[T, T], img2: np.ndarray[T, T]) -> bool:
    return (img1 == img2).all()
        

def main(data: str) -> int:
    """part 1 of the puzzle """
    return sum(r.row*100 + r.col for r in map(partial(find_reflection, validator=is_reflection), process_data(data)))


def test() -> bool:
    return main(test_input) == 405


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
