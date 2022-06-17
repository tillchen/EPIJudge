from typing import List

from test_framework import generic_test

import bintrees

def find_closest_elements_in_sorted_arrays(sorted_arrays: List[List[int]]) -> int:
    result = float('inf')
    iters = bintrees.RBTree()
    for i, sorted_array in enumerate(sorted_arrays):
        it = iter(sorted_array)
        sorted_array_min = next(it, None)
        if sorted_array_min is not None:
            iters.insert((sorted_array_min, i), it)

    while True:
        min_value, min_index = iters.min_key()
        max_value = iters.max_key()[0]
        result = min(result, max_value - min_value)
        it = iters.pop_min()[1]
        next_min = next(it, None)
        if next_min is None:
            return result
        iters.insert((next_min, min_index), it)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_distance_3_sorted_arrays.py',
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
