# https://adventofcode.com/2023/day/23
from __future__ import annotations
from typing import Callable
from aoc_utils import test_input, get_raw_data, process_data, neighbors, ir
from aoc_recipes import Point, where, progress_bar, where2


def dfs[T](ini: T, fin: T, grafo: dict[T, dict[T, int]], seen: set[T] = None, callback: Callable[[], None] = None) -> int:
    if ini == fin:
        return 0
    if seen is None:
        seen = set()
    if callback:
        callback()
    result = float("-inf")
    seen.add(ini)
    for p in grafo[ini]:
        if p in seen:
            continue
        result = max(result, grafo[ini][p] + dfs(p, fin, grafo, seen, callback))
    seen.remove(ini)
    return result


def main(data: str):
    """part 2 of the puzzle """
    # https://www.youtube.com/watch?v=NTLYL7Mg2jU
    img = process_data(data)
    start = Point(0, next(where(img[0,:]=="."))[0])
    end_x = img.shape[0] - 1
    goal = Point(end_x, next(where(img[end_x,:]=="."))[0])
    img[img!="#"]="."

    cross_road = [p for p in where2(img==".") if p in {start, goal} or ir.ilen(neighbors(p, img)) > 2]

    # edge contraction
    grafo: dict[Point, dict[Point, int]] = {p: {} for p in cross_road}

    for c in cross_road:
        stack = [(0, c)]
        seen = {c}
        while stack:
            d, p = stack.pop()
            if d and p in cross_road:
                grafo[c][p] = d
                continue
            for v in neighbors(p, img):
                if v not in seen:
                    stack.append((d+1, v))
                    seen.add(v)

    with progress_bar() as bar:
        return dfs(start, goal, grafo, callback=lambda: bar.update(1))


def test() -> bool:
    return main(test_input) == 154


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
