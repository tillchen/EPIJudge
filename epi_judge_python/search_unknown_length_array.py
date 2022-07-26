from typing import List

from test_framework import generic_test
from bisect import bisect_left


def binary_search_unknown_length(A: List[int], k: int) -> int:
    return bisect_left(A, k) if k in A else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_unknown_length_array.py',
                                       'search_unknown_length_array.tsv',
                                       binary_search_unknown_length))
