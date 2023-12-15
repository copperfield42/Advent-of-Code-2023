# https://adventofcode.com/2023/day/15
from typing import Iterable


test_input = """
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""


def lens_hash(data: str | Iterable[str]) -> int:
    result = 0
    for c in map(ord, data):
        result = ((c+result)*17) % 256
    return result


def process_data(data: str) -> list[str]:
    """transform the raw data into a processable form"""
    return data.strip().split(",")


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
