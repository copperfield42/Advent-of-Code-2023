#https://adventofcode.com/2023/day/8
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, test_input_2, MOVES, ir



def walk(instrucciones:tuple[int,...], network:dict[str,tuple[str,str]], inicial:str="AAA" ) -> Iterable[str]:
    node = inicial
    moves = ir.cycle(instrucciones)
    while True:
        yield node
        node = network[node][next(moves)]

    


def main(data:str) -> int:
    """part 1 of the puzzle """
    return ir.ilen(ir.takewhile(lambda x:x!="ZZZ",walk(*process_data(data))))


def test() -> bool:
    return main(test_input) == 2 and main(test_input_2) == 6



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # 
    












