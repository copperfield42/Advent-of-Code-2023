# https://adventofcode.com/2023/day/11
from __future__ import annotations

from typing import Iterable
import itertools_recipes as ir
import numpy as np


test_input = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""


def process_data(data: str) -> np.ndarray[bool, bool]:
    """transform the raw data into a processable form"""
    return np.array([[ c=="#" for c in line] for line in ir.interesting_lines(data)], dtype=bool)


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
