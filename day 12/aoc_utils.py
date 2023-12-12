# https://adventofcode.com/2023/day/12
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
from ast import literal_eval


test_input = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""


def process_data(data: str) -> Iterable[tuple[str, tuple[int, ...]]]:
    """transform the raw data into a processable form"""
    for line in ir.interesting_lines(data):
        format1, format2 = line.split()
        yield format1, literal_eval(format2)
    pass


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
