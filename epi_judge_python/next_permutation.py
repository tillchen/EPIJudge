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
    if turning_point == len(perm) - 1:
        swap_index = turning_point - 1
    else:
        swap_target = min(x for x in perm[turning_point + 1:] if x > perm[turning_point])
        swap_index = perm.index(swap_target, turning_point+1)
    result = perm[:]
    result[turning_point], result[swap_index] = result[swap_index], result[turning_point]
    result[turning_point + 1:] = sorted(result[turning_point + 1:])
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
