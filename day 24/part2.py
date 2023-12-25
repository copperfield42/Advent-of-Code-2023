# https://adventofcode.com/2023/day/24
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from dataclasses import dataclass
from aoc_recipes import Point3
from functools import cached_property
from itertools_recipes import dotproduct
import sympy


@dataclass(frozen=True)
class Recta3:
    ini: Point3
    vector: Point3

    @cached_property
    def m(self) -> Point3:
        # https://en.wikipedia.org/wiki/Pl%C3%BCcker_coordinates
        return self.ini.cross_product(self.ini + self.vector)

    def __contains__(self, item: Point3) -> bool:
        if isinstance(item, Point3):
            return dotproduct(item, self.m) == 0
        return False

    def __call__(self, *arg) -> Point3:
        if len(arg) == 1:
            time = arg[0]
            return self.ini + time * self.vector
        p = x, y, z = arg
        a, b, c, d = self.coeff
        return x*a + y*b + z*c + d


def main(data: str) -> int:
    """part 2 of the puzzle """
    granizos = [Recta3(p, v) for p, v in process_data(data)]

    xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr", integer=True)

    equations = []
    for i, g in enumerate(granizos, 1):
        s = g.ini
        v = g.vector
        equations.append((xr - s.x) * (v.y - vyr) - (yr - s.y) * (v.x - vxr))
        equations.append((yr - s.y) * (v.z - vzr) - (zr - s.z) * (v.y - vyr))
        if len(equations) < 6:
            continue
        result = [s for s in sympy.solve(equations)]
        if len(result) == 1:
            print(f"needed {i=} granizos")
            break
    ans = result[0]
    print(ans)
    return ans[xr] + ans[yr] + ans[zr]


def test() -> bool:
    return main(test_input) == 47


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
