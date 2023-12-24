# https://adventofcode.com/2023/day/24
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
from ast import literal_eval
from aoc_recipes import Point3


test_input = """
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""


def process_data(data: str) -> Iterable[tuple[Point3, Point3]]:
    """transform the raw data into a processable form"""
    for line in ir.interesting_lines(data):
        a, b = line.split("@")
        yield Point3(*literal_eval(a)), Point3(*literal_eval(b))
    pass


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
