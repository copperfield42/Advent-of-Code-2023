# https://adventofcode.com/2023/day/21
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_recipes import where2, make_vecinos


def main(data: str, num_steps: int = 64) -> int:
    """part 1 of the puzzle """
    img = process_data(data)
    start = next(where2(img=="S"))
    img[start] = "."
    reached = {start}
    garden_plots = set(where2(img=="."))
    for _ in range(num_steps):
        reached = {v for p in reached for v in make_vecinos(p, garden_plots.__contains__)}
    return len(reached)


def test() -> bool:
    return main(test_input, 6) == 16


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
