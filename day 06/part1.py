#https://adventofcode.com/2023/day/6
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
import operator, math

dist = operator.mul


def race(tiempo:int, distancia:int) -> int:
    return sum(distancia < dist(velocidad,tiempo-velocidad) for velocidad in range(1,tiempo))


def main(data:str) -> int:
    """part 1 of the puzzle """
    return math.prod(map(race,*process_data(data)))


def test() -> bool:
    return main(test_input) == 288



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # 
    












