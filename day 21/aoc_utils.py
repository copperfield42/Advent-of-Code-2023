# https://adventofcode.com/2023/day/21
from __future__ import annotations
import itertools_recipes as ir
import numpy as np


test_input = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""


def process_data(data: str) -> np.ndarray[str, str]:
    """transform the raw data into a processable form"""
    return np.array([list(line) for line in ir.interesting_lines(data)], dtype=str)


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
