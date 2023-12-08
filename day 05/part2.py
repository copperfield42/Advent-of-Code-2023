#https://adventofcode.com/2023/day/5
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, Almanac
from collections_recipes import CompactRange
import itertools
import aoc_recipes


def main_brute(data:str) -> int:
    """part 2 of the puzzle """
    seed_pairs, *almanacs = process_data(data)
    seeds = CompactRange.from_pairs( (ini,ini+size-1) for ini, size in  itertools.batched(seed_pairs,2))
    print(seeds, len(seeds))
    for alma in aoc_recipes.progress_bar(almanacs, position=0):
        new = CompactRange()
        for s in aoc_recipes.progress_bar(seeds, position=1, leave=False):
            new.add(alma.map(s))
        seeds = new
    print(seeds, len(seeds))
    return seeds[0]


def ranges_manipulation(data:CompactRange, transformation:Almanac) -> CompactRange:
    maps = transformation.get_range_maps()
    pendiente = data.to_pairs()
    new = set()
    while pendiente:
        ran = pendiente.pop()
        ini, fin = ran
        for from_ran, to_ran in maps:
            a,b = from_ran[0], from_ran[-1]
            #is totally contain
            if a <= ini and fin<=b:
                new.add( (to_ran[from_ran.index(ini)], to_ran[from_ran.index(fin)]) )
                break
            #is partially contain
            a,b = from_ran[0], from_ran[-1]
            if a<=ini<=b and b<fin:
                pendiente.append( (ini,b) )
                pendiente.append( (b+1,fin) )
                break
            if ini<a and a<=fin<=b:
                pendiente.append( (ini,a-1) )
                pendiente.append( (a,fin) )
                break
        else:#if no break
            new.add( ran )
    return CompactRange.from_pairs(new)
    pass

def main(data:str) -> int:
    """part 2 of the puzzle """
    seed_pairs, *almanacs = process_data(data)
    seeds = CompactRange.from_pairs( (ini,ini+size-1) for ini, size in  itertools.batched(seed_pairs,2))
    #print(seeds, len(seeds))
    for alma in almanacs:
        seeds = ranges_manipulation(seeds, alma)
    #print(seeds, len(seeds))
    return seeds[0]

def test() -> bool:
    return main(test_input) == 46



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #
    













