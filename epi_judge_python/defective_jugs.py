import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Jug = collections.namedtuple('Jug', ('low', 'high'))


def check_feasible(jugs: List[Jug], L: int, H: int) -> bool:
    VolumeRange = collections.namedtuple('VolumeRange', ('low', 'high'))
    memo = set()
    def helper(L: int, H: int) -> bool:
        if L > H or VolumeRange(L, H) in memo or (L < 0 and H < 0):
            return False
        if any((L <= j.low and j.high <= H) or helper(L - j.low, H - j.high) for j in jugs):
            return True
        memo.add(VolumeRange(L, H))
        return False
    return helper(L, H)


@enable_executor_hook
def check_feasible_wrapper(executor, jugs, l, h):
    jugs = [Jug(*x) for x in jugs]
    return executor.run(functools.partial(check_feasible, jugs, l, h))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('defective_jugs.py',
                                       'defective_jugs.tsv',
                                       check_feasible_wrapper))
