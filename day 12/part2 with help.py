# https://adventofcode.com/2023/day/12
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from functools import cache


def unfold(arrange: str, config: tuple[int, ...]) -> tuple[str, tuple[int, ...]]:
    return "?".join(arrange for _ in range(5)), config*5


@cache
def count_arranges(arrange: str, config: tuple[int]) -> int:
    # https://www.youtube.com/watch?v=g3Ms5e7Jdqo
    if not arrange:
        return 0 if config else 1
    if not config:
        # any remaining ? is treated as .
        return 0 if "#" in arrange else 1
    
    result = 0

    if arrange[0] in ".?":
        # treat any ? as . and/or remove a sequences of dots
        result += count_arranges(arrange[1:].lstrip("."), config)

    if arrange[0] in "#?":
        # treat any ? as #
        eaten, left = arrange[:config[0]], arrange[config[0]:]
        if config[0] <= len(arrange) and "." not in eaten:
            if len(arrange) == config[0] or left[0] != "#":
                result += count_arranges(left[1:], config[1:])

    return result

        
def main(data: str) -> int:
    """part 2 of the puzzle """
    return sum(count_arranges(*unfold(*line)) for line in process_data(data))


def test() -> bool:
    return main(test_input) == 525152


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  # 160500973317706
