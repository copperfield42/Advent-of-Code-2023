# https://adventofcode.com/2023/day/23
from __future__ import annotations
from aoc_utils import test_input, get_raw_data, process_data, longest_path_grafo
from aoc_recipes import where, Point


def main(data: str) -> int:
    """part 1 of the puzzle """
    img = process_data(data)
    start = Point(0, next(where(img[0,:]=="."))[0])
    end_x = img.shape[0] - 1
    goal = Point(end_x, next(where(img[end_x,:]=="."))[0])
    print(img.shape)
    return longest_path_grafo(start, goal, img)


def test() -> bool:
    return main(test_input) == 94


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
