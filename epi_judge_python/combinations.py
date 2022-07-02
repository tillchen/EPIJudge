from typing import List

from test_framework import generic_test, test_utils

import itertools


def combinations_0(n: int, k: int) -> List[List[int]]:
    return list(map(list, itertools.combinations(range(1, n + 1), k)))

def combinations(n: int, k: int) -> List[List[int]]:
    result = []
    def helper(offset: int, partial_combination: List[int]):
        if len(partial_combination) == k:
            result.append(list(partial_combination))
            return
        num_remaining = k - len(partial_combination)
        i = offset
        while i <= n and num_remaining <= n + 1 - i:
            helper(i + 1, partial_combination + [i])
            i += 1
    helper(1, [])
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
