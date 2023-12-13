# https://adventofcode.com/2023/day/13
from __future__ import annotations

from typing import Iterable, NamedTuple, Callable
import itertools_recipes as ir
import numpy as np


test_input = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""


class ReflectData(NamedTuple):
    row: int
    col: int


def find_reflection[T](image: np.ndarray[T, T], validator: Callable[[np.ndarray[T, T], np.ndarray[T, T]], bool]) -> ReflectData:
    x, y = image.shape
    # search vertical reflection
    for col in range(1, y):
        size = min(abs(y-col), col)
        a = image[:, col-size:col]
        b = image[:, col:col+size]
        if validator(a, b[:, ::-1]):
            return ReflectData(0, col)
    # search horizontal reflection
    for row in range(1, x):
        size = min(abs(x-row), row)
        a = image[row-size:row, :]
        b = image[row:row+size, :]
        if validator(a, b[::-1, :]):
            return ReflectData(row, 0)
    return ReflectData(0, 0)


def process_data(data: str) -> Iterable[np.ndarray[bool, bool]]:
    """transform the raw data into a processable form"""
    for table in ir.isplit(data.splitlines()):
        yield np.array([[e == "#" for e in row] for row in table], dtype=bool)
    pass


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
