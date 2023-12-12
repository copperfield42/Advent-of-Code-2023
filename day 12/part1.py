# https://adventofcode.com/2023/day/12
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, ir
from aoc_recipes import progress_bar

def is_valid(arrange: str, config: tuple[int, ...]) -> bool:
    return all(a==b for a,b in zip((ir.ilen(v) for k,v in ir.groupby(arrange) if k=="#"),config, strict=True))


def produce_valid_arranges(arrange: str, config: tuple[int, ...]) -> Iterable[str]:
    if "?" in arrange:
        for c in "#.":
            new = arrange.replace("?", c, 1)
            yield from produce_valid_arranges(new, config)
    else:
        try:
            if is_valid(arrange, config):
                yield arrange
        except ValueError:
            pass


def main(data: str) -> int:
    """part 1 of the puzzle """
    return sum(ir.ilen(produce_valid_arranges(*line)) for line in progress_bar(tuple(process_data(data))))


def test() -> bool:
    return main(test_input) == 21


if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
