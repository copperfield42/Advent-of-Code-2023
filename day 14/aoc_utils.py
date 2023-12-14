# https://adventofcode.com/2023/day/14
from __future__ import annotations

import itertools_recipes as ir
from aoc_recipes import where2, DIRECCIONES, is_valid
from collections import deque
import numpy as np


def tilting_north(data: np.ndarray[str, str]) -> np.ndarray[str, str]:
    """tilting north in place"""
    shape = data.shape
    to_move = deque(where2(data == "O"))
    data[data == "O"] = "."
    direc = DIRECCIONES["^"]
    while to_move:
        p = to_move.popleft()
        while is_valid((new := p+direc), shape) and data[new] == ".":
            p = new
        data[p] = "O"
    return data


def total_load(data: np.ndarray[str, str]) -> int:
    return sum(p.x+1 for p in where2(data[::-1, :] == "O"))


test_input = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""


def process_data(data: str) -> np.ndarray[str, str]:
    """transform the raw data into a processable form"""
    return np.array([list(line) for line in ir.interesting_lines(data)], dtype=str)


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
