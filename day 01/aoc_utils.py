#https://adventofcode.com/2023/day/1
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir





test_input="""
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""



def process_data(data:str) -> Iterable[tuple[str,...]]:
    """transform the raw data into a procesable form"""
    for line in ir.interesting_lines(data):
        yield tuple(filter(str.isdigit,line))
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()


#-------------------------------------------------------------------------------


