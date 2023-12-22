# https://adventofcode.com/2023/day/22
from __future__ import annotations
from typing import Iterable
from aoc_utils import test_input, get_raw_data, process_data, Brick
from aoc_recipes import Point3, progress_bar
from dataclasses import dataclass


def settle_bricks(iterable: Iterable[Point3]) -> list[Point3]:
    result = []
    for b in iterable:
        while b.high[0] > 1:
            new = b.move_vertically(-1)
            if any(x.collide(new) for x in result):
                break
            else:
                b = new
        result.append(b)
    return result



def main(data: str) -> int:
    """part 1 of the puzzle """
    initial: list[Brick] = sorted(progress_bar(process_data(data), desc="reading"), key=lambda b: b.high[0])
    settle = settle_bricks(progress_bar(initial, desc="settling"))
    result = 0
    for to_destroy in progress_bar(settle):
        new = [x for x in settle if x != to_destroy]
        settle_new = settle_bricks(new)
        result += new == settle_new
    print(f"{result=}")
    return result


def test() -> bool:
    return main(test_input) == 5


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
