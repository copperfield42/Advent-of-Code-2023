#https://adventofcode.com/2023/day/6
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
import num_bases, functools
import part1

def num_concat(nums:tuple[int]) -> int:
    return functools.reduce(num_bases.num_concat,nums)


def main(data:str) -> int:
    """part 2 of the puzzle """
    time, dist = map(num_concat, process_data(data))
    #print(f"{time=} {dist=}")
    
    return part1.race(time, dist)


def test() -> bool:
    return main(test_input) == 71503



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #
    













