#https://adventofcode.com/2023/day/2
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
import operator, functools, math

def find_power(data:Counter) -> int:
    return math.prod(data.values())


def main(data:str) -> int:
    """part 2 of the puzzle """
    return sum(find_power(functools.reduce(operator.or_,game)) for game in process_data(data))


def test() -> bool:
    return main(test_input) == 2286



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #
    













