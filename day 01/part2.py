#https://adventofcode.com/2023/day/1
from __future__ import annotations

from aoc_utils import get_raw_data, ir





test_input="""
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

spell_nums = "one two three four five six seven eight nine"
table = {k:str(v) for v,k in enumerate(spell_nums.split(),1)}
table.update( (n,n) for n in map(str,range(1,10)) )

def extract(text:str) -> tuple[str,str]:
    def filter_out(iterable, index):
        return ( x for x in iterable if x[index]>=0 )
    result = [(text.find(k),text.rfind(k),v) for k,v in table.items()]       
    return (
        min(filter_out(result,0),key=lambda x:x[0])[-1],
        max(filter_out(result,1),key=lambda x:x[1])[-1]
        )

def process_data(data:str) -> Iterable[tuple[str,...]]:
    """transform the raw data into a procesable form"""
    for line in ir.interesting_lines(data):
        yield extract(line)
        
    
    


def main(data:str) -> int:
    """part 2 of the puzzle """
    return sum( int(line[0] + line[-1]) for line in process_data(data))


def test() -> bool:
    return main(test_input) == 281



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #
    













