#https://adventofcode.com/2023/day/3
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
import aoc_recipes
import re
from aoc_recipes import Point



test_input="""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

DIRECCIONES = frozenset(aoc_recipes.DIRECCIONES["*"])

def process_line(text_line:str, line_number:int=0) -> Iterable[ tuple[int, frozenset[Point]] | tuple[str, Point] ]:
    for find in re.finditer(r"(\d+|[^\d\.])",text_line):
        symbol, start, end = find.group(), find.start(), find.end()
        if symbol.isdigit():
            #symbol = int(symbol)
            yield int(symbol), frozenset(Point(x,line_number) for x in range(start, end))
        else:
            assert end - start == 1
            yield symbol, Point(start, line_number)
                

def process_data(data:str) -> tuple[tuple[tuple[int, frozenset[Point]] | tuple[str, Point]],...]:
    """transform the raw data into a procesable form"""
    for y, line in enumerate(ir.interesting_lines(data)):
        yield tuple(process_line(line, y))
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()


#-------------------------------------------------------------------------------


