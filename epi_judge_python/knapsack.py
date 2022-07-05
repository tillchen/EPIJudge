import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    memo = {}
    def helper(k: int, capacity: int) -> int:
        if k < 0:
            return 0
        if (k, capacity) not in memo:
            without_current_item = helper(k - 1, capacity)
            with_current_item = 0 if capacity < items[k].weight else items[k].value + helper(k - 1, capacity - items[k].weight)
            memo[(k, capacity)] = max(with_current_item, without_current_item)
        return memo[(k, capacity)]
    return helper(len(items) - 1, capacity)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
