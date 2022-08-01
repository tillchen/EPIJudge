from typing import List

from test_framework import generic_test
from typing import Callable


def max_subarray_sum_in_circular(A: List[int]) -> int:
    def find_optimal_subarray(f: Callable) -> int:
        current_optimum = result = 0
        for x in A:
            current_optimum = f(x, x + current_optimum)
            result = f(result, current_optimum)
        return result
    return max(find_optimal_subarray(max), sum(A) - find_optimal_subarray(min))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'maximum_subarray_in_circular_array.py',
            'maximum_subarray_in_circular_array.tsv',
            max_subarray_sum_in_circular))
