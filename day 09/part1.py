#https://adventofcode.com/2023/day/9
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, ir


def predictor(seq:tuple[int,...]) -> int:
    prev_seq = seq
    last = [prev_seq[-1]]
    while True:
        next_seq = [b-a for a,b in ir.pairwise(prev_seq)]
        if not any(next_seq):
            break
        prev_seq = next_seq
        last.append(prev_seq[-1])
    return sum(last)



def main(data:str) -> int:
    """part 1 of the puzzle """
    return sum(map(predictor, process_data(data)))


def test() -> bool:
    return main(test_input) == 114



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # 
    












