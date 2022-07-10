from typing import List

from test_framework import generic_test


def longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    memo = [1] * len(A)
    for i in range(1, len(A)):
        memo[i] = 1 + max([memo[j] for j in range(i) if A[j] <= A[i]], default=0)
    return max(memo)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_nondecreasing_subsequence.py',
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
