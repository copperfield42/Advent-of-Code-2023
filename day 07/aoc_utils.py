#https://adventofcode.com/2023/day/7
from __future__ import annotations

from typing import Iterator, Iterable, NamedTuple
import itertools_recipes as ir
import num_bases

camel_cards = '23456789TJQKA'
camel_symbols = dict(zip(camel_cards,range(20)))

class CamelCard(NamedTuple):
    hand: str
    bid: int


def from_camel(hand:str, symbols:dict[str,int]=camel_symbols) -> int:
    "give a numeric value to a this hand"
    return num_bases.fromBase(hand,len(symbols),symbols=symbols)


def processed_hand_type(hand:list[int]) -> int:
    match hand:
        case [5]: #5 of a kind
            return 6 
        case [1,4]: #4 of a kind
            return 5 
        case [2,3]: #full house
            return 4
        case [1,1,3]:#3 of a kind
            return 3
        case [1,2,2]:#2 pairs
            return 2 
        case [1,1,1,2]:#1 pair
            return 1
        case [1,1,1,1,1]:#high card
            return 0
        case error:
            raise ValueError(f"Invalid processed hand {hand=} (the list should be ordered and at most of 5 elements)")




test_input="""
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""



def process_data(data:str) -> Iterable[CamelCard]:
    """transform the raw data into a procesable form"""
    for line in ir.interesting_lines(data):
        h,b = line.split()
        yield CamelCard(h, int(b))
    pass
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()


#-------------------------------------------------------------------------------


