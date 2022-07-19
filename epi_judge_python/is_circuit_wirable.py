import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

from collections import deque

class GraphVertex:
    def __init__(self) -> None:
        self.d = -1
        self.edges: List[GraphVertex] = []


def is_any_placement_feasible(graph: List[GraphVertex]) -> bool:
    def bfs(v: GraphVertex):
        queue = deque([v])
        v.d = 0
        while queue:
            current = queue.popleft()
            for vertex in current.edges:
                if vertex.d == -1:
                    vertex.d = current.d + 1
                    queue.append(vertex)
                else:
                    if vertex.d == current.d:
                        return False
        return True
    return all(bfs(v) for v in graph if v.d == -1)


@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_circuit_wirable.py',
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))
