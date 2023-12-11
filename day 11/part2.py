# https://adventofcode.com/2023/day/11
from __future__ import annotations

from aoc_utils import test_input, get_raw_data
import part1


def main(data: str, expansion_factor: int = 10**6) -> int:
    """part 2 of the puzzle """
    return part1.main(data, (expansion_factor-1) if expansion_factor > 1 else 1)


def test() -> bool:
    return main(test_input, 100) == 8410 and main(test_input, 10) == 1030


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
    













