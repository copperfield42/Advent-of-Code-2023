#https://adventofcode.com/2023/day/3
#from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, DIRECCIONES, Point, Iterable


def get_matchs[N:tuple[int, frozenset[Point]], S:tuple[str, Point]](data_num:set[N], data_sym:set[S]) -> Iterable[N]:
    for np in data_num:
        num, points = np
        for sym, point in data_sym:
            if any( ((p-point) in DIRECCIONES) for p in points):
                yield np
        

def main(data:str) -> int:
    """part 1 of the puzzle """
    result = 0
    prev_num = set()
    prev_sym = set()
    for line in process_data(data):
        current_num = set()
        current_sym = set()
        for item in line:
            if isinstance(item[0],int):
                current_num.add(item)
            else:
                current_sym.add(item)
        matchs = set(get_matchs(current_num|prev_num, current_sym|prev_sym))
        current_num.difference_update(matchs)
        result += sum(np[0] for np in matchs)
        prev_num, prev_sym = current_num, current_sym
    return result


def test() -> bool:
    return main(test_input) == 4361



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # 
    












