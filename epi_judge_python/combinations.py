from typing import List

from test_framework import generic_test, test_utils

import itertools


def combinations(n: int, k: int) -> List[List[int]]:
    return list(map(list, itertools.combinations(range(1, n + 1), k)))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
