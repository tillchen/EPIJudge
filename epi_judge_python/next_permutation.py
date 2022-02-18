from tracemalloc import start
from typing import List

from test_framework import generic_test


# [6, 2, 1, 5, 4, 3, 0] -> [6, 2, 3, 0, 1, 4, 5]
def next_permutation(perm: List[int]) -> List[int]:
    turning_point = None
    for i in reversed(range(len(perm) - 1)):
        if perm[i] < perm[i + 1]:
            turning_point = i
            break
    if turning_point is None:
        return []
    result = perm[:]
    if turning_point == len(perm) - 2:
        result[turning_point], result[turning_point + 1] = result[turning_point + 1], result[turning_point]
        return result
    # Since the suffix is decreasing, the first (in the reverse order) element bigger than turning_point is our swap.
    for i in reversed(range(turning_point + 1, len(perm))):
        if result[i] > result[turning_point]:
            result[turning_point], result[i] = result[i], result[turning_point]
            break
    result[turning_point + 1:] = reversed(result[turning_point + 1:])
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
