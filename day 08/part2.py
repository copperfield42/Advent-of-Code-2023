#https://adventofcode.com/2023/day/8
from __future__ import annotations

from aoc_utils import get_raw_data, process_data, ir
from part1 import walk
import aoc_recipes
import math

test_input = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

def terminate(step:tuple[str,...]) -> bool:
    return not all(s.endswith("Z") for s in step)

def main_brute(data:str) -> int:
    """part 2 of the puzzle """
    inst, network = process_data(data)
    iniciales = [walk(inst,network,node) for node in network if node.endswith("A")]
    return ir.ilen(ir.takewhile(terminate,aoc_recipes.progress_bar(zip(*iniciales))))


def cycle_size(instrucciones:tuple[int,...], network:dict[str,tuple[str,str]], inicial:str) -> int:
    pasos = {}
    n = len(instrucciones)
    for i,step in enumerate(zip(walk(instrucciones,network,inicial),ir.cycle(range(n)))):
        if step in pasos:
            return len(pasos) - pasos[step]
        pasos[step] = i

def main(data:str) -> int:
    """part 2 of the puzzle """
    inst, network = process_data(data)
    cycles_size = [cycle_size(inst,network,node) for node in network if node.endswith("A")]
    return math.lcm(*cycles_size)


def test() -> bool:
    return main(test_input) == 6



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", result:=main(data), f"({result:_})") #
    













