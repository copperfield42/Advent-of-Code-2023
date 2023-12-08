#https://adventofcode.com/2023/day/5
from __future__ import annotations

from typing import Iterator, Iterable, NamedTuple
import itertools_recipes as ir


class AlmanacRange(NamedTuple):
    destination: int
    source: int
    length: int
    
    def map(self, value:int) -> int:
        s = range(self.source, self.source + self.length )
        if value in s:
            p = s.index(value)
            return range(self.destination, self.destination + self.length)[p]
        return -1
    
    def get_range_map(self) -> tuple[range,range]:
        return range(self.source, self.source + self.length ), range(self.destination, self.destination + self.length)

class Almanac(NamedTuple):
    maptype: str
    ranges: list[AlmanacRange] 
    
    def map(self, value:int) -> int:
        for alra in self.ranges:
            v = alra.map(value)
            if v != -1:
                return v
        return value
    
    def get_range_maps(self) -> list[tuple[range,range]]:
        return sorted((r.get_range_map() for r in self.ranges), key=lambda x:x[0][0])




test_input="""
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""



def process_data(data:str) -> Iterable[Almanac | tuple[int,...]]:
    """transform the raw data into a procesable form"""
    for line in ir.isplit(map(str.strip,data.splitlines())):
        if line[0].startswith("seeds:"):
            name, nums = line[0].split(":")
            yield tuple(map(int, nums.split()))
        else:
            name, *nums = line
            yield Almanac(
                      name.replace(" map:",""), 
                      [AlmanacRange(*map(int, seg.split())) for seg in nums]
                      )
    pass
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()


#-------------------------------------------------------------------------------


