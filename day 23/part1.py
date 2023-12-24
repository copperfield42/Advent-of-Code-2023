# https://adventofcode.com/2023/day/23
from __future__ import annotations
from aoc_utils import test_input, get_raw_data, process_data, neighbors
from aoc_recipes import where, Point
from contextlib import contextmanager
import sys


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


@contextmanager
def set_recursion_limit(limit):
    old = sys.getrecursionlimit()
    new = max(limit, old)
    try:
        sys.setrecursionlimit(new)
        yield
    finally:
        sys.setrecursionlimit(old)


def longest_path_grafo(inicio: Point, goal: Point, matrix: np.ndarray[str, str]) -> int:
    # https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/
    stack = []
    visited = set()
    dist = Distances()
    with set_recursion_limit(matrix.shape[0]*matrix.shape[1]):
        topologicalSortUtil(inicio, stack, visited, matrix)

    dist[inicio] = 0

    while stack:
        u = stack.pop()
        if dist[u] != float("-inf"):
            for i in neighbors(u, matrix):
                new = dist[u] + 1
                if dist[i] < new:
                    dist[i] = new
    return dist[goal]


def main(data: str) -> int:
    """part 1 of the puzzle """
    img = process_data(data)
    start = Point(0, next(where(img[0,:]=="."))[0])
    end_x = img.shape[0] - 1
    goal = Point(end_x, next(where(img[end_x,:]=="."))[0])
    print(img.shape)
    return longest_path_grafo(start, goal, img)


def test() -> bool:
    return main(test_input) == 94


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
