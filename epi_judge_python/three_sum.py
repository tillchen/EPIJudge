from typing import List

from test_framework import generic_test
from two_sum import has_two_sum


def has_three_sum(A: List[int], t: int) -> bool:
    A.sort()
    return any(has_two_sum(A, t - x) for x in A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
