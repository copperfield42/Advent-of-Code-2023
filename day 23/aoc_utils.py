# https://adventofcode.com/2023/day/23
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
import numpy as np
from aoc_recipes import vecinos, is_valid, DIRECCIONES, Point
import sys


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


def topologicalSortUtil(v: Point, stack: list[Point], visited: set[Point], matrix: np.ndarray[str, str]):
    # https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/
    visited.add(v)
    for i in neighbors(v, matrix):
        if i in visited:
            continue
        topologicalSortUtil(i, stack, visited, matrix)
    stack.append(v)


class Distances(dict):

    def __missing__(self, key):
        return float("-inf")


def longest_path_grafo(inicio: Point, goal: Point, matrix: np.ndarray[str, str]) -> int:
    # https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/
    stack = []
    visited = set()
    dist = Distances()

    old_re_li = sys.getrecursionlimit()
    new_re_li = max(old_re_li, matrix.shape[0]*matrix.shape[1])
    sys.setrecursionlimit(new_re_li)

    topologicalSortUtil(inicio, stack, visited, matrix)

    sys.setrecursionlimit(old_re_li)

    dist[inicio] = 0

    while stack:
        u = stack.pop()
        if dist[u] != float("-inf"):
            for i in neighbors(u, matrix):
                new = dist[u] + 1
                if dist[i] < new:
                    dist[i] = new
    return dist[goal]


def process_data(data: str) -> np.ndarray[str, str]:
    """transform the raw data into a processable form"""
    return np.array([ list(line) for line in ir.interesting_lines(data)], dtype=str)


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
