#https://adventofcode.com/2023/day/1
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data





def main(data:str) -> int:
    """part 1 of the puzzle """
    return sum( int(line[0] + line[-1]) for line in process_data(data))


def test() -> bool:
    return main(test_input) == 142



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # 
    












