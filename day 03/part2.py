#https://adventofcode.com/2023/day/3
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, DIRECCIONES, Point, Iterable
from collections import defaultdict
import math



def get_matchs[N:tuple[int, frozenset[Point]], S:tuple[str, Point]](data_num:set[N], data_sym:set[S]) -> Iterable[tuple[S,N]]:
    for np in data_num:
        num, points = np
        for sym in data_sym:
            point = sym[1]
            if any( ((p-point) in DIRECCIONES) for p in points):
                yield sym, np
        



def main(data:str) -> int:
    """part 2 of the puzzle """
    result = 0
    prev_num = set()
    prev_sym = set()
    matchs = defaultdict(set)
    for line in process_data(data):
        current_num = set()
        current_sym = set()
        for item in line:
            if isinstance(item[0],int):
                current_num.add(item)
            elif item[0]=="*":
                current_sym.add(item)
        for sym, nps in get_matchs( prev_num|current_num, prev_sym|current_sym ):
            matchs[sym].add(nps)
        prev_num, prev_sym = current_num, current_sym
    return sum( math.prod(np[0] for np in nps) for nps in matchs.values() if len(nps)==2)


def test() -> bool:
    return main(test_input) == 467835



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #
    













