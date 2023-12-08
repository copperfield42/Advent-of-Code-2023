#https://adventofcode.com/2023/day/5
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, AlmanacRange, Almanac





def main(data:str) -> int:
    """part 1 of the puzzle """
    seeds, *almanacs = process_data(data)
    for alma in almanacs:
        seeds = [alma.map(s) for s in seeds]
    return min(seeds)


def test() -> bool:
    return main(test_input) == 35



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # 
    












