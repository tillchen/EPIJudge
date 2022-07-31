from typing import List

from test_framework import generic_test


def count_inversions(A: List[int]) -> int:
    result = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] > A[j] and i < j:
                result += 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_inversions.py',
                                       'count_inversions.tsv',
                                       count_inversions))
