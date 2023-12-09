# https://adventofcode.com/2023/day/9
from __future__ import annotations

from typing import Iterable, Sequence
import itertools_recipes as ir


test_input = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""


def seq_diff(seq: Sequence[int]) -> Iterable[list[int]]:
    while any(seq):
        seq = [b-a for a, b in ir.pairwise(seq)]
        yield seq


def process_data(data: str) -> Iterable[tuple[int, ...]]:
    """transform the raw data into a processable form"""
    for line in ir.interesting_lines(data):
        yield tuple(map(int, line.split()))
    pass
    
    
def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
