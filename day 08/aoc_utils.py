#https://adventofcode.com/2023/day/8
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
import re 


MOVES = {"R":1, "L":0}


test_input="""
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

test_input_2="""
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""



def process_data(data:str) -> tuple[tuple[int,...], dict[str,tuple[str,str]]]:
    """transform the raw data into a procesable form"""
    iter_lines = ir.interesting_lines(data)
    instruciones = next(iter_lines)
    network = {a:(b,c) for a,b,c in (re.findall(r"\w+",line) for line in iter_lines)}
    return tuple(map(MOVES.get,instruciones)), network
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()


#-------------------------------------------------------------------------------


