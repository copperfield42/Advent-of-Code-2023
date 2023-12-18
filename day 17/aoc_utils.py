# https://adventofcode.com/2023/day/17
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
import numpy as np


test_input = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""


def process_data(data: str) -> np.ndarray[int, int]:
    """transform the raw data into a processable form"""
    return np.array([list(map(int, line)) for line in ir.interesting_lines(data)], dtype=int)


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
