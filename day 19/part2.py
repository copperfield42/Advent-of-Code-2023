# https://adventofcode.com/2023/day/19
from __future__ import annotations

from typing import Iterable, Any, Self
from aoc_utils import test_input, get_raw_data, process_data, DelayedOP, OPERATION
import operator
from dataclasses import dataclass, asdict, astuple

OPPOSITE = {
    "<": operator.ge,
    ">": operator.le,
    }


@dataclass
class XMAS:
    x: tuple[Any] | None
    m: tuple[Any] | None
    a: tuple[Any] | None
    s: tuple[Any] | None

    def __getitem__(self, item):
        if item in "xmas":
            return getattr(self, item)
        raise KeyError(item)

    def __iter__(self):
        return iter(astuple(self))

    def set(self, key, value) -> Self:
        d = asdict(self)
        d[key] = value
        return type(self)(**d)


def walk_flow(workflows: dict[str, list[tuple[DelayedOP, str] | str]], start="in", xmas: XMAS = XMAS(None, None, None, None)) -> Iterable[XMAS]:
    if start == "A":
        yield xmas
        return
    if start == "R":
        return
    for item in workflows[start]:
        if isinstance(item, tuple):
            dop: DelayedOP
            dop, news = item
            val = dop.value
            opp = OPPOSITE[">"] if OPERATION[">"] is dop.op else OPPOSITE["<"]
            if xmas[dop.key] is None:
                yield from walk_flow(workflows, news, xmas.set(dop.key, ((dop.op, val),)))
                xmas = xmas.set(dop.key, ((opp, val),))
            else:
                yield from walk_flow(workflows, news, xmas.set(dop.key, xmas[dop.key] + ((dop.op, val),)))
                xmas = xmas.set(dop.key, xmas[dop.key]+((opp, val),))
        else:
            yield from walk_flow(workflows, item, xmas)


def calculate_xmas(data: XMAS, min_val: int = 1, max_val: int = 4000) -> int:
    ran = range(min_val, max_val+1)
    total = 1
    for val in data:
        if val is None:
            total *= len(ran)
        else:
            value = 0
            for n in ran:
                for op, cmp in val:
                    if not op(n, cmp):
                        break
                else:  # no break
                    value += 1
            total *= value
        if not total:
            break
    return total


def main(data: str) -> int:
    """part 2 of the puzzle """
    workflows, _ = process_data(data)
    return sum(map(calculate_xmas, walk_flow(workflows)))


def test() -> bool:
    return main(test_input) == 167409079868000


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
