# https://adventofcode.com/2023/day/23
from __future__ import annotations

from typing import Iterable
import itertools_recipes as ir
import numpy as np
from aoc_recipes import vecinos, is_valid, DIRECCIONES, Point


test_input = """
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
"""


def neighbors(p: Point, matrix: np.ndarray[str, str]) -> Iterable[Point]:
    for new in vecinos(p):
        if not is_valid(new, matrix.shape):
            continue
        if matrix[new] == "#":
            continue
        if matrix[new] in "<>^v":
            move = new - p
            if DIRECCIONES[matrix[new]] != move:
                continue
        yield new


def process_data(data: str) -> np.ndarray[str, str]:
    """transform the raw data into a processable form"""
    return np.array([ list(line) for line in ir.interesting_lines(data)], dtype=str)


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
