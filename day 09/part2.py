#https://adventofcode.com/2023/day/9
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, ir


def predictor_back(seq:tuple[int,...]) -> int:
    prev_seq = seq
    first = [prev_seq[0]]
    while True:
        next_seq = [b-a for a,b in ir.pairwise(prev_seq)]
        if not any(next_seq):
            break
        prev_seq = next_seq
        first.append(prev_seq[0])
    result = 0
    for x in reversed(first):
        result = x-result
    return result



def main(data:str) -> int:
    """part 2 of the puzzle """
    return sum(map(predictor_back, process_data(data)))


def test() -> bool:
    return main(test_input) == 2



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #
    













