from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int], n: int) -> None:
    i, j, write_index = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if A[i] > B[j]:
            A[write_index] = A[i]
            i -= 1
        else:
            A[write_index] = B[j]
            j -= 1
        write_index -= 1
    while j >= 0:
        A[write_index] = B[j]
        j -= 1
        write_index -= 1


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
