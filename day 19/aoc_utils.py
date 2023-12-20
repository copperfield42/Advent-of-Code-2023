# https://adventofcode.com/2023/day/19
from __future__ import annotations

from typing import NamedTuple, Callable, Self
import itertools_recipes as ir
import operator


test_input = r"""
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""


OPERATION = {
    "<": operator.lt,
    ">": operator.gt,
    }


class DelayedOP(NamedTuple):
    op: Callable[[int, int], bool]
    key: str
    value: int

    def __call__(self, value):
        return self.op(value, self.value)

    @classmethod
    def from_str(cls, text: str) -> Self:
        for op in OPERATION:
            if op in text:
                x, y = text.split(op)
                return cls(OPERATION[op], x.strip(), int(y))
        raise ValueError(f"Unknown operation in text: {text!r}")


def flow(workflows: dict[str, list[tuple[DelayedOP, str] | str]], rating: dict[str, int], start="in") -> int:
    while start not in {"A", "R"}:
        work = workflows[start]
        for item in work:
            if isinstance(item, tuple):
                dop, re = item
                if dop(rating[dop.key]):
                    start = re
                    break
            else:
                start = item
                break
    if start == "R":
        return 0
    return sum(rating.values())


def process_data(data: str) -> tuple[dict[str, list[tuple[DelayedOP, str] | str]], list[dict[str, int]]]:
    """transform the raw data into a processable form"""
    workflows_raw, ratings_raw = ir.isplit(data.strip().splitlines())
    workflows: dict[str, list[tuple[DelayedOP, str] | str ]] = {}
    line: str
    for line in workflows_raw:
        name, ins_raw = line.split("{")
        ins = []
        for text in ins_raw.replace("}", "").split(","):
            if ":" in text:
                k, v = text.split(":")
                ins.append((DelayedOP.from_str(k), v.strip()))
            else:
                ins.append(text.strip())
        workflows[name.strip()] = ins

    ratings: list[dict[str, int]] = [{k.strip(): int(v) for k, v in (kv.split("=") for kv in line[1:-1].split(","))}
                                     for line in ratings_raw]
    return workflows, ratings


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
