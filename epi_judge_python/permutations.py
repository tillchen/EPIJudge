from typing import List

from test_framework import generic_test, test_utils

import itertools

from next_permutation import next_permutation


def permutations_0(A: List[int]) -> List[List[int]]:
    return [list(x) for x in itertools.permutations(A)]

def permutations_1(A: List[int]) -> List[List[int]]:
    result = []
    def helper(i: int):
        if i == len(A) - 1:
            result.append(A.copy())
            return
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            helper(i + 1)
            A[j], A[i] = A[i], A[j]
    helper(0)
    return result

def permutations(A: List[int]) -> List[List[int]]:
    result = []
    while True:
        result.append(A.copy())
        A = next_permutation(A)
        if not A:
            break
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
