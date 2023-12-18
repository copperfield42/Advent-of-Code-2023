# https://adventofcode.com/2023/day/18
from __future__ import annotations
from typing import Iterable
import itertools_recipes as ir
from aoc_recipes import DIRECCIONES, Point


MOVES = {
    "U": DIRECCIONES["^"],
    "D": DIRECCIONES["v"],
    "L": DIRECCIONES["<"],
    "R": DIRECCIONES[">"],
    }


test_input = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""


def process_data(data: str) -> Iterable[tuple[Point, int, str]]:
    """transform the raw data into a processable form"""
    for line in ir.interesting_lines(data):
        move, n, rgb = line.split()
        yield MOVES[move], int(n), rgb[2:-1]
    pass


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
