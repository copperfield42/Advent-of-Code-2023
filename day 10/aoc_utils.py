# https://adventofcode.com/2023/day/10
from __future__ import annotations

from typing import Iterable, overload, Any
import itertools_recipes as ir
import numpy as np
import aoc_recipes
from aoc_recipes import Point, DIRECCIONES, is_valid
from collections.abc import Sequence


test_input = """
.....
.S-7.
.|.|.
.L-J.
.....
"""

test_input_2 = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""


def walk(maze: np.ndarray[str, str], start: Point, initial_dir: Point) -> Iterable[Point]:
    pos = start
    move = initial_dir
    yield pos
    while True:
        new = pos + move
        if not is_valid(new, maze.shape):
            raise IndexError("outside of the maze")
        if maze[new] == "|" and move in {DIRECCIONES["v"], DIRECCIONES["^"]}:
            pos = new
        elif maze[new] == "-" and move in {DIRECCIONES["<"], DIRECCIONES[">"]}:
            pos = new
        elif maze[new] == "L" and move in {DIRECCIONES["v"], DIRECCIONES["<"]}:
            pos = new
            move = DIRECCIONES[">"] if move == DIRECCIONES["v"] else DIRECCIONES["^"]
        elif maze[new] == "J" and move in {DIRECCIONES["v"], DIRECCIONES[">"]}:
            pos = new
            move = DIRECCIONES["<"] if move == DIRECCIONES["v"] else DIRECCIONES["^"]
        elif maze[new] == "7" and move in {DIRECCIONES["^"], DIRECCIONES[">"]}:
            pos = new
            move = DIRECCIONES["<"] if move == DIRECCIONES["^"] else DIRECCIONES["v"]
        elif maze[new] == "F" and move in {DIRECCIONES["^"], DIRECCIONES["<"]}:
            pos = new
            move = DIRECCIONES[">"] if move == DIRECCIONES["^"] else DIRECCIONES["v"]
        elif maze[new] == ".":
            raise ValueError("find ground")
        elif maze[new] == "S":
            pos = new
            yield pos
            return
        else:
            raise ValueError("invalid move")
        yield pos
        if pos == start:
            return


class MazePath(Sequence[Point]):

    def __init__(self, path: Iterable[Point]):
        self._data = tuple(path)

    @overload
    def __getitem__(self, index: int) -> Point: ...

    @overload
    def __getitem__(self, index: slice) -> tuple[Point,...]: ...

    def __getitem__(self, index: int | slice) -> Point | tuple[Point, ...]:
        return self._data[index]

    def __len__(self) -> int:
        return len(self._data)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, type(self)):
            return False
        return sorted(self._data) == sorted(other._data)

    def __iter__(self) -> Iterable[Point]:
        return iter(self._data)

    def __hash__(self) -> int:
        return hash(frozenset(self._data))

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._data})"


def find_max_path(start: Point, maze: np.ndarray[str, str]) -> MazePath:
    paths = set()
    for dir_move in DIRECCIONES["+"]:
        try:
            paths.add(MazePath(walk(maze, start, dir_move)))
        except (ValueError, IndexError):
            pass
    return max(paths, key=len)


def process_data(data: str) -> tuple[Point, np.ndarray[str, str]]:
    """transform the raw data into a processable form"""
    maze = np.array([list(line) for line in ir.interesting_lines(data)], dtype=str)
    s = Point(*next(aoc_recipes.where(maze == "S")))
    return s, maze


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
