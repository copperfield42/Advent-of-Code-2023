# https://adventofcode.com/2023/day/22
from __future__ import annotations
from aoc_utils import test_input, get_raw_data, process_data, settle_bricks, settle_bricks_it
from aoc_recipes import progress_bar


def main(data: str) -> int:
    """part 2 of the puzzle """
    initial = sorted(progress_bar(process_data(data), desc="reading"), key=lambda b: b.high[0])
    settle = settle_bricks(progress_bar(initial, desc="settling"))
    result = 0
    check = {b.brick_id: b for b in settle}
    for to_destroy in progress_bar(settle, desc="working"):
        new = [x for x in settle if x != to_destroy]
        for b in settle_bricks_it(new):
            if check[b.brick_id] != b:
                result += 1
    return result


def test() -> bool:
    return main(test_input) == 7


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
