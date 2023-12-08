#https://adventofcode.com/2023/day/7
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, processed_hand_type, from_camel
from collections import Counter
import part1

camel_cards_2 = 'J23456789TQKA'
camel_symbols_2 = dict(zip(camel_cards_2,range(20)))

def from_camel_2(hand:str):
    return from_camel(hand, symbols=camel_symbols_2)

def hand_type_2(hand:str) -> int:
    J = hand.count("J")
    new_hand = hand.replace("J","")
    if new_hand:
        processed_hand = sorted(Counter(new_hand).values())
        processed_hand[-1] += J
    else:
        processed_hand = [J]
    return processed_hand_type(processed_hand)

def main(data:str) -> int:
    """part 2 of the puzzle """
    return part1.main(data, hand_type=hand_type_2, from_camel=from_camel_2)


def test() -> bool:
    return main(test_input) == 5905



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #
    













