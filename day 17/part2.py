# https://adventofcode.com/2023/day/17
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
import part1


test_input_2 = """
111111111111
999999999991
999999999991
999999999991
999999999991
"""



def main(data: str) -> int:
    """part 2 of the puzzle """
    return part1.main(data, 4, 10)


def test() -> bool:
    return main(test_input) == 94 and main(test_input_2) == 71



if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  # 980
    













