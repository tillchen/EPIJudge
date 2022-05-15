from typing import List

from test_framework import generic_test
import heapq

def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    sorted_lists = []
    INCREASING, DECREASING = 0, 1
    array_type = INCREASING
    start_index = 0
    for i in range(1, len(A) + 1):
        if (i == len(A)
            or array_type == INCREASING and A[i] < A[i - 1]
            or array_type == DECREASING and A[i] > A[i - 1]
        ):
            sorted_lists.append(A[start_index:i] if array_type == INCREASING else A[i-1:start_index-1:-1])
            start_index = i
            array_type = INCREASING if array_type == DECREASING else DECREASING
    return list(heapq.merge(*sorted_lists))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
