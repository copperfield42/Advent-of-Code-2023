#https://adventofcode.com/2023/day/7
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, from_camel, processed_hand_type
from collections import Counter



def hand_type(hand:str) -> int:
    return processed_hand_type(sorted(Counter(hand).values()))


def main(data:str, *, hand_type=hand_type, from_camel=from_camel) -> int:
    """part 1 of the puzzle """
    return sum( rank*play.bid for rank,play in enumerate(sorted(process_data(data), key=lambda c:(hand_type(c.hand),from_camel(c.hand))),1))


def test() -> bool:
    return main(test_input) == 6440



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # 
    












