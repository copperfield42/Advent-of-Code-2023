#https://adventofcode.com/2023/day/6
from __future__ import annotations

from typing import Iterator, Iterable, NamedTuple
import itertools_recipes as ir


class RaceData(NamedTuple):
    time: tuple[int]
    distance: tuple[int]


test_input="""
Time:      7  15   30
Distance:  9  40  200
"""



def process_data(data:str) -> RaceData:
    """transform the raw data into a procesable form"""
    return RaceData(*(tuple(map(int,line.split(":")[1].split())) for line in ir.interesting_lines(data)))
#        name, nums = line.split()
#        yield name, tuple(map(int,nums.split()))
    pass
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()


#-------------------------------------------------------------------------------


