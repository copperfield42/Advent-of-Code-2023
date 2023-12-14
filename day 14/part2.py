# https://adventofcode.com/2023/day/14
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, tilting_north, total_load
from aoc_recipes import progress_bar, where2
import numpy as np


def tilting_cycle(data: np.ndarray[str, str]) -> np.ndarray[str, str]:
    data = tilting_north(data)
    data = tilting_north(np.rot90(data, axes = (1,0)))  # tilting west
    data = tilting_north(np.rot90(data, axes = (1,0)))  # tilting south
    data = tilting_north(np.rot90(data, axes = (1,0)))  # tilting east
    return np.rot90(data, axes = (1,0))


def main(data: str, show: bool = False) -> int:
    """part 2 of the puzzle """
    img = process_data(data)
    steps = {}
    pasos = []
    period = []
    total_cicles = 10**9
    for n in progress_bar(range(total_cicles)):
        new = tilting_cycle(img)
        tl = total_load(new)
        snapshot = tuple(where2(new == "O")), tl
        if snapshot in steps:
            rep = steps[snapshot]
            period = pasos[rep:]
            pasos = pasos[:rep]
            if show:
                print(f"find cycle size {len(steps)-rep} of {len(steps)=} at {rep=}")
            break
        steps[snapshot] = n
        pasos.append(tl)
        img = new
    else:  # no break
        return total_load(img)
    pos = (total_cicles-len(pasos)-1) % len(period)
    if show:
        print(f"{pos=}")
        print(f"{pasos=}\n\n{period=}\n")
    return period[pos]    


def test() -> bool:
    return main(test_input) == 64


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
