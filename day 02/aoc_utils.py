#https://adventofcode.com/2023/day/2
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
from collections import Counter





test_input="""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

COLORS = ("green", "red", "blue")

def get_plays(text:str) -> Counter[str]:
    result = {c:0 for c in COLORS}
    for segment in text.split(","):
        n, color = segment.split()
        result[color] = int(n)
    return Counter(result)


def process_data(data:str) -> tuple[Counter[str],...]:
    """transform the raw data into a procesable form"""
    for line in ir.interesting_lines(data):
        _, games = line.split(": ",maxsplit=1)
        yield tuple(get_plays(g) for g in games.split(";"))
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()


#-------------------------------------------------------------------------------


