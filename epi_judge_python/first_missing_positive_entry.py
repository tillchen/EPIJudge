from typing import List

from test_framework import generic_test


def find_first_missing_positive_0(A: List[int]) -> int:
    A = [x for x in sorted(set(A)) if x > 0]
    result = 1
    for x in A:
        if x != result:
            return result
        result += 1
    return result

def find_first_missing_positive_1(A: List[int]) -> int:
    set_of_A = set(A)
    result = 1
    while result in set_of_A:
        result += 1
    return result

def find_first_missing_positive(A: List[int]) -> int:
    for i in range(len(A)):
        while 1 <= A[i] <= len(A) and A[i] != A[A[i] - 1]:
            A[A[i] - 1], A[i] = A[i], A[A[i] - 1]
    for i, x in enumerate(A):
        if x != i + 1:
            return i + 1
    return len(A) + 1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('first_missing_positive_entry.py',
                                       'first_missing_positive_entry.tsv',
                                       find_first_missing_positive))
