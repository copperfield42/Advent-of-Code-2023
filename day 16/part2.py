# https://adventofcode.com/2023/day/16
from __future__ import annotations
from typing import Iterable, TypeAlias
from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import energize, DIRECCIONES, Point
from aoc_recipes import progress_bar

Move: TypeAlias = Point


def border_points(x: int, y: int) -> Iterable[tuple[Point, Move]]:
    for n in range(x):
        yield Point(n, 0), DIRECCIONES[">"]
        yield Point(n, y-1), DIRECCIONES["<"]
    for m in range(y):
        yield Point(0, m), DIRECCIONES["v"]
        yield Point(x-1, m), DIRECCIONES["^"]
    

def main(data: str) -> int:
    """part 2 of the puzzle """
    img = process_data(data)
    return max(energize(img, p, m).sum() for p, m in progress_bar(border_points(*img.shape), total=sum(2*s for s in img.shape)))


def test() -> bool:
    return main(test_input) == 51


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
