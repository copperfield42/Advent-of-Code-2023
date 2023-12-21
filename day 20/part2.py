# https://adventofcode.com/2023/day/20
from __future__ import annotations

from aoc_utils import get_raw_data, process_data, Signal, pprint
import itertools
from aoc_recipes import progress_bar
import math


class StarON(Exception):
    pass


class Destination:

    def __call__(self, data: Signal) -> list[Signal]:
        if not data.pulse:
            raise StarON
        return []


def main_brute(data: str) -> int:
    """part 2 of the puzzle """
    machine = process_data(data)
    dest = Destination()
    pprint(machine.modules)
    for i in progress_bar(itertools.count(1)):
        try:
            machine(output=dest)
        except StarON:
            return i
    return -1


def main(data: str) -> int:
    """part 2 of the puzzle """
    # https://www.youtube.com/watch?v=lxm6i21O83k
    machine = process_data(data)
    output = "rx"
    ((feed),) = [mod.name for mod in machine.modules.values() if output in mod.connected]
    cycle_length = {}
    seen = {mod.name: 0 for mod in machine.modules.values() if feed in mod.connected}
    print(f"feed into rx: {feed} {seen=}")

    def callback(sig: Signal):
        nonlocal presses
        if sig.receptor == feed and sig.pulse:
            seen[sig.sender] += 1
            if sig.sender not in cycle_length:
                cycle_length[sig.sender] = presses
            if all(seen.values()):
                raise StarON(f"found all cycles")

    for presses in itertools.count(1):
        try:
            machine(callback=callback)
        except StarON as result:
            print(presses, result, cycle_length, seen)
            return math.lcm(*cycle_length.values())


if __name__ == "__main__":
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
