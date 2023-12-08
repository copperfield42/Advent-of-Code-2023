#https://adventofcode.com/2023/day/4
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from collections import Counter




def main(data:str) -> int:
    """part 2 of the puzzle """
    n = 0
    scratchcards = Counter()
    for n,card in enumerate(process_data(data)):
        scratchcards[n] += 1
        hits = sum( n in card.winners for n in card.numbers)
        for s in range(1,1+hits):
            scratchcards[n+s] += scratchcards[n]
    to_drop = [d for d in scratchcards if d>n]
    for d in to_drop:
        del scratchcards[d]
    return scratchcards.total()


def test() -> bool:
    return main(test_input) == 30



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #
    













