# https://adventofcode.com/2023/day/17
from __future__ import annotations
from typing import Iterable, Any
from aoc_utils import test_input, get_raw_data, process_data, ir
from aoc_recipes import Point, shortest_path_grafo, make_vecinos, is_valid, PriorityQueue, DIRECCIONES, progress_bar
import aoc_recipes
import numpy as np
from functools import partial
from operator import eq


def neighbors[Path: tuple[Point, ...]](path: Path, grafo: np.ndarray[int,int], min_len:int=1, max_len:int=3) -> Iterable[tuple[Path,int]]:
    validator = partial(is_valid, shape=grafo.shape)
    last = path[-1]
    for move in DIRECCIONES["+"]:
        new = last + move
        try:
            if new == path[-2]:
                continue
        except IndexError:
            pass
            if move != DIRECCIONES[">"]:
                continue
        new_paths = [(new,)]
        for n in range(max_len):
            new_paths.append( new_paths[-1] + (new_paths[-1][-1]+move,) )
        for p in new_paths:
            if len(p) < min_len:
                continue
            if all(validator(x) for x in p):
                yield path + p, len(p)

            
            
def cost[Path: tuple[Point,...]](old_path:Path, new_path: Path, old_cost: int, grafo: np.ndarray[int, int], max_len:int=3) -> int:
    for k,v in ir.groupby( p1-p2 for p1,p2 in ir.pairwise(new_path)):
        if ir.ilen(v) > max_len :
            return float("inf")
    return old_cost + sum(grafo[p] for p in (set(new_path)-set(old_path)))



def shortest_path_matrix[Matrix:np.ndarray[Any, Any], Path:tuple[Point, ...], Cost:int](
    inicio: Point,
    meta: Point,
    tablero: Matrix,
    neighbors: Callable[[Path, Matrix], Iterable[Path]],
    cost: Callable[[Path, Path, Cost, Matrix], Cost],
    initial_cost: Cost = 0,
    callback=None) -> tuple[Cost, Path]:
    #https://www.youtube.com/watch?v=sBe_7Mzb47Y
    visitado = set()
    is_meta = partial(eq, meta)
    queue = PriorityQueue()
    queue.add_task( (initial_cost,(inicio,),Point(0,0),0), initial_cost )
    while queue:
        record = queue.pop_task()
        old_cost, path, dir_move, num_step = record  # @hyper-neutrino in youtube
        if (path[-1], dir_move, num_step) in visitado:
            continue
        visitado.add((path[-1], dir_move, num_step))
        if callback:
            callback(meta.distance_t(path[-1]))
        if is_meta(path[-1]):
            return old_cost, path
        for new_path, n in neighbors(path, tablero):
            new_cost = cost(path, new_path, old_cost, tablero)
            new_record = new_cost, new_path, new_path[-1]-new_path[-2], n
            queue.add_task( new_record, new_cost )
    return float("inf"), None


def callback_bar(pbar:progress_bar, progress:int):
        pbar.n = pbar.total - progress
        pbar.update()

def show_path(tablero: np.ndarray[Any, Any], path: Iterable[Point]):
    mapa = np.zeros_like(tablero, dtype=bool)
    for p in path:
        mapa[p] = True
    return aoc_recipes.show_bool_matrix2(mapa)

expected_raw = """
2>>34^>>>1323
32v>>>35v5623
32552456v>>54
3446585845v52
4546657867v>6
14385987984v4
44578769877v6
36378779796v>
465496798688v
456467998645v
12246868655<v
25465488877v5
43226746555v>
"""
expected = np.array([[not x.isdigit() for x in line] for line in ir.interesting_lines(expected_raw)], dtype=bool)
expected[0,0]=True

def main(data: str, min_len:int=1, max_len:int=3) -> int:
    """part 1 of the puzzle """
    img = process_data(data)
    ini = Point(0,0)
    goal = Point(*img.shape)-Point(1,1)
    with aoc_recipes.progress_bar(total=ini.distance_t(goal)) as bar:
        result = shortest_path_matrix(ini, goal, img, partial(neighbors, min_len=min_len, max_len=max_len), partial(cost, max_len=max_len), callback = partial(callback_bar,bar))
    return result[0]


def test() -> bool:
    return main(test_input) == 102


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  # 855
