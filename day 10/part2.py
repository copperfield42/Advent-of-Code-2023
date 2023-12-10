# https://adventofcode.com/2023/day/10
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, walk, MazePath, find_max_path, test_input_2, Point, ir
import aoc_recipes
import numpy as np
from aoc_recipes import DIRECCIONES

test_input_3 = """
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""

test_input_4 = """
..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........
"""

test_input_5 = """
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
"""

test_input_6 = """
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""


def inflate(path:MazePath, maze:np.ndarray[str,str]) -> np.ndarray[bool,bool]:
    x = max(p.x for p in path)+1
    y = max(p.y for p in path)+1
    pshape = (3+x*3, 3+y*3)
    plain = np.zeros(pshape, dtype=bool)
    validator = lambda p: aoc_recipes.is_valid(p,pshape)
    for p in path:
        new = p*3+(1+1j)
        plain[new] = True
        match maze[p]:
            case "S":
                for v in aoc_recipes.make_vecinos(new, validator, direcciones=DIRECCIONES["*"]):
                    plain[v]=True
            case "|":
                plain[new + DIRECCIONES["^"]] = True
                plain[new + DIRECCIONES["v"]] = True
            case "-":
                plain[new + DIRECCIONES["<"]] = True
                plain[new + DIRECCIONES[">"]] = True
            case "L":
                plain[new + DIRECCIONES["^"]] = True
                plain[new + DIRECCIONES[">"]] = True
            case "J":
                plain[new + DIRECCIONES["^"]] = True
                plain[new + DIRECCIONES["<"]] = True
            case "7":
                plain[new + DIRECCIONES["<"]] = True
                plain[new + DIRECCIONES["v"]] = True
            case "F":
                plain[new + DIRECCIONES[">"]] = True
                plain[new + DIRECCIONES["v"]] = True
    return plain


def desinflate(matrix:np.ndarray[bool,bool]) -> np.ndarray[bool. bool]:
    X,Y = matrix.shape
    result = np.zeros(((X-3)//3, (Y-3)//3), dtype=bool)
    

def fill_gass(matrix:np.ndarray[bool, bool], initial:Point=Point(0,0)) -> np.ndarray[bool,bool]:
    result = np.zeros_like(matrix, dtype=bool)
    points = set(ir.starmap(Point, aoc_recipes.where(~matrix)))
    work = {initial}
    while work:
        p = work.pop()
        result[p] = True
        points.discard(p)
        work.update(np for np in aoc_recipes.vecinos(p) if np in points)
    return result
    

def show(matrix:np.ndarray[bool,bool]):
    X,Y = matrix.shape
    for x in range(X):
        for y in range(Y):
            print(aoc_recipes.BLACK_char if matrix[x,y] else aoc_recipes.WHITE_char, sep="",end="")
        print()
    print()

def main(data: str, mostrar:bool=False) -> int:
    """part 2 of the puzzle """
    S, maze = process_data(data)
    path = find_max_path(S, maze)
    plain = inflate(path, maze)
    if mostrar: show(plain)
    outside = fill_gass(plain)
    if mostrar: show(filled)
    result = 0
    X,Y = maze.shape
    for x in range(X):
        for y in range(Y):
            p = Point(x,y)
            if p in path:
                continue
            ip = p*3+(1+1j)
            if aoc_recipes.is_valid(ip, outside.shape):
                if not outside[ip]:
                    result +=1
                    
    return result


def test() -> bool:
    tests=[
        (test_input_3,4),
        (test_input_4,4),
        (test_input_5,8),
        (test_input_6,10),
        ]
    return all(main(t)==r for t,r in tests)



if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
    













