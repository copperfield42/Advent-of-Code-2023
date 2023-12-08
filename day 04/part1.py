#https://adventofcode.com/2023/day/4
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data





def main(data:str) -> int:
    """part 1 of the puzzle """
    result = 0
    for card in process_data(data):
        hits = sum( n in card.winners for n in card.numbers)
        if hits:
            result += 2**(hits-1)
    return result


def test() -> bool:
    return main(test_input) == 13



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # 
    












