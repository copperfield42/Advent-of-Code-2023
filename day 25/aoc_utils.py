# https://adventofcode.com/2023/day/25
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir


test_input = """
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
"""


def process_data(data: str) -> dict[str, set[str]]:
    """transform the raw data into a processable form"""
    result = {}
    for line in ir.interesting_lines(data):
        line = line.replace(":"," ")
        k, *v = line.split()
        #result.setdefault(k, dict()).update((x, None) for x in v)
        result.setdefault(k, set()).update(v)
    return result


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
