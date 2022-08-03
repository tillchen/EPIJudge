from typing import List

from test_framework import generic_test


def max_square_submatrix(A: List[List[bool]]) -> int:
    pre = [0] * len(A[0])
    max_side = 0
    for row in A:
        for j, v in enumerate(row[1:], 1):
            row[j] *= min(pre[j - 1], pre[j], row[j - 1]) + 1
        max_side = max(max_side, max(row))
        pre = row
    return max_side**2


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_square_submatrix.py',
                                       'max_square_submatrix.tsv',
                                       max_square_submatrix))
