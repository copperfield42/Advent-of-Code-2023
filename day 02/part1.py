#https://adventofcode.com/2023/day/2
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, Counter





def main(data:str, **config) -> int:
    """part 1 of the puzzle """
    rule = Counter(**config)
    return sum( i for i,game in enumerate(process_data(data),1) if all(ronda<=rule for ronda in game))


def test() -> bool:
    return main(test_input, red=12, green=13, blue=14) == 8



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data, red=12, green=13, blue=14)) # 
    












