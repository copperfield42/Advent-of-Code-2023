# https://adventofcode.com/2023/day/15
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, lens_hash
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Lens:
    name: str
    focal: int

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        return super().__eq__(other)


def main(data: str) -> int:
    """part 2 of the puzzle """
    hashmap = defaultdict(list)
    for ins in process_data(data):
        if "-" in ins:
            label = ins[:-1]
            focal_len = None
        elif "=" in ins:
            label, focal = ins.split("=")
            focal_len = int(focal)
        else:
            raise ValueError(f"invalid instruction: {ins!r}")
        hash_label = lens_hash(label)
        if focal_len is None:
            try:
                hashmap[hash_label].remove(label)
            except ValueError:
                pass
        else:
            new = Lens(label, focal_len)
            try:
                i = hashmap[hash_label].index(label)
            except ValueError:
                hashmap[hash_label].append(new)
            else:  # no error
                hashmap[hash_label][i] = new
    return sum((k+1)*i*x.focal for k, v in hashmap.items() for i, x in enumerate(v, 1))


def test() -> bool:
    return main(test_input) == 145


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
