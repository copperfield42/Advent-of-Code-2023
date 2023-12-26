# https://adventofcode.com/2023/day/25
from __future__ import annotations
from typing import Callable, Iterable

import networkx

from aoc_utils import test_input, get_raw_data, process_data
from collections import defaultdict, Counter
from pprint import pprint
from dataclasses import dataclass
from aoc_recipes import set_recursion_limit, shortest_path_grafo
from itertools import combinations
import networkx as nx


@dataclass
class NodeStatus[T]:
    node: T
    index: int = None
    lowlink: int = None
    onStack: bool = False





def tarjan_strongly_connected_components[G, V](grafo: G, nodes: Callable[[G], Iterable[V]], successors: Callable[[G, V], Iterable[V]] ):
    """https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm"""
    def strongconnect(v: NodeStatus):
        nonlocal index, stack
        # Set the depth index for v to the smallest unused index
        v.index = index
        v.lowlink = index
        index += 1
        stack.append(v)
        v.onStack = True

        # Consider successors of v
        for nw in successors(grafo, v.node):
            w = vertices[nw]
            if w.index is None:
                # Successor w has not yet been visited; recurse on it
                strongconnect(w)
                v.lowlink = min(v.lowlink, w.lowlink)
            elif w.onStack:
                # Successor w is in stack S and hence in the current SCC
                # If w is not on stack, then (v, w) is an edge pointing to an SCC already found and must be ignored
                # The next line may look odd - but is correct.
                # It says w.index not w.lowlink; that is deliberate and from the original paper
                v.lowlink = min(v.lowlink, w.index)
        # If v is a root node, pop the stack and generate an SCC
        if v.lowlink == v.index:
            scc = []
            while True:
                w = stack.pop()
                w.onStack = False
                #scc.append(w)#.node)
                scc.append(w.node)
                if w is v:
                    break
            return scc

    index = 0
    stack = []
    vertices: dict[V, NodeStatus[V]] = {k: NodeStatus(k) for k in nodes(grafo)}
    #pprint(vertices)
    with set_recursion_limit(len(vertices)):
        for ver in vertices.values():
            if ver.index is None:
                yield strongconnect(ver)










def main2(data: str) -> int:
    """part 1 of the puzzle """
    grafo = process_data(data)
    items = [(k, tuple(v)) for k, v in grafo.items()]

    for k,v in items:
        for x in v:
            grafo.setdefault(x, dict())[k]=None#.add(k)
    print(f"{len(grafo)=}")

    tscc = list(tarjan_strongly_connected_components(grafo, iter, dict.get))
    assert len(tscc) == 1
    scc = tscc[0]

    lowlink = Counter(w.lowlink for w in tscc[0])
    print(f"{lowlink=}")
    lowlink_con = defaultdict(set)
    for v in scc:
        lowlink_con[v.lowlink].add(v.node)
    print("lowlink_con=")
    pprint(lowlink_con)

    travel = defaultdict(dict)
    for a, b in combinations(grafo,2):
        if a == b:
            continue
        dist = shortest_path_grafo(a, b, grafo, lambda p, g: g[p])
        travel[a][b] = dist[0]
        travel[b][a] = dist[0]
        travel[a][a] = 0
    #print("travel=")
    #pprint(travel)
    max_lowlink = {}
    lowlink_to_check = sorted(lowlink)
    del lowlink_to_check[0]
    print(f"{lowlink_to_check=}")
    for x in reversed(lowlink_to_check):
        for n in lowlink_con[x]:
            d = max(travel[n][y] for y in lowlink_con[0] )
            print(d, {n:[k for k,v in travel[n].items() if v<d and k not in lowlink_con[0]]})
        break


    return



def main(data: str) -> int:
    """part 1 of the puzzle """
    grafo = process_data(data)
    items = [(k, tuple(v)) for k, v in grafo.items()]

    for k, v in items:
        for x in v:
            grafo.setdefault(x, set()).add(k)
    print(f"{len(grafo)=}")

    grafonx = networkx.from_dict_of_lists(grafo)
    print(grafonx)
    mec = networkx.minimum_edge_cut(grafonx)
    assert len(mec) == 3
    print("edges tu cut:", mec)
    for a, b in mec:
        grafo[a].discard(b)
        grafo[b].discard(a)

    scc = tuple(tarjan_strongly_connected_components(grafo, iter, dict.get))
    assert len(scc) == 2
    par1, par2 = scc
    print(f"{len(par1)=} {par1=}\n{len(par2)=} {par2=}")

    return len(par1) * len(par2)


def test() -> bool:
    return main(test_input) == 54


if __name__ == "__main__":
    assert test(), "fail test part 1"
    test()
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
