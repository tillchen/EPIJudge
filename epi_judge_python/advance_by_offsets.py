from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    # e.g. [3, 3, 1, 0, 2, 0, 1] returns true. A[0] -> A[1] -> A[4] -> A[6]. current_max = [3, 4, 4, 4, 6, 0, 7]
    # e.g. [3, 2, 0, 0, 2, 0, 1] returns false. current_max = [3, 3, 3, 3]
    current_max = 0
    i = 0
    while i <= current_max and current_max < len(A) - 1:
        current_max = max(current_max, i + A[i])
        i += 1
    return current_max >= len(A) - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
