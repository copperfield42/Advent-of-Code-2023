# https://adventofcode.com/2023/day/16
from __future__ import annotations
import itertools_recipes as ir
from aoc_recipes import DIRECCIONES, Point, is_valid, show_bool_matrix2
import numpy as np

test_input = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""

MOVES = {DIRECCIONES[k]: k for k in "<>v^"}


def energize(data: np.ndarray[str, str], initial: Point = Point(0, 0), direction: Point = DIRECCIONES[">"], show: bool = False) -> np.ndarray[bool, bool]:
    result = np.zeros_like(data, dtype=bool)
    beans = [(initial, direction)]
    seen_beans = set()
    while beans:
        p, move = beans.pop()
        result[p] = True
        if show and data[p] != ".":
            print(data[p], p, MOVES[move], [(xp, MOVES[m]) for xp, m in beans])
            show_bool_matrix2(result)
        if (p,move) in seen_beans:
            if show:
                print("discarded", data[p], p, MOVES[move], [(xp, MOVES[m]) for xp, m in beans])
            continue
        else:
            seen_beans.add((p, move))
        new = None
        new_moves = None
        match data[p]:
            case ".":
                new = p + move
            case "|":
                if move in {DIRECCIONES[">"], DIRECCIONES["<"]}:
                    new_moves = DIRECCIONES["^"], DIRECCIONES["v"]
                else:
                    new = p + move
            case "-":
                if move in {DIRECCIONES["v"], DIRECCIONES["^"]}:
                    new_moves = DIRECCIONES["<"], DIRECCIONES[">"]
                else:
                    new = p + move
            case "\\":
                if move == DIRECCIONES[">"]:
                    move = DIRECCIONES["v"]
                elif move == DIRECCIONES["<"]:
                    move = DIRECCIONES["^"]
                elif move == DIRECCIONES["^"]:
                    move = DIRECCIONES["<"]
                elif move == DIRECCIONES["v"]:
                    move = DIRECCIONES[">"]
                else:
                    raise ValueError(f"invalid move direction {move!r}")
                new = p + move
            case "/":
                if move == DIRECCIONES[">"]:
                    move = DIRECCIONES["^"]
                elif move == DIRECCIONES["<"]:
                    move = DIRECCIONES["v"]
                elif move == DIRECCIONES["^"]:
                    move = DIRECCIONES[">"]
                elif move == DIRECCIONES["v"]:
                    move = DIRECCIONES["<"]
                else:
                    raise ValueError(f"invalid move direction {move!r}")
                new = p + move
        if new is not None:
            if is_valid(new, data.shape):
                beans.append((new, move))
        elif new_moves is not None:
            for m in new_moves:
                new = p + m
                if is_valid(new, data.shape):
                    beans.append((new, m))
        else:
            raise RuntimeError("invalid state")
    return result


def process_data(data: str) -> np.ndarray[str, str]:
    """transform the raw data into a processable form"""
    return np.array([list(line) for line in ir.interesting_lines(data)], dtype=str)


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
