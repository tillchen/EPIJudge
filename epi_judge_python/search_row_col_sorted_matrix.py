from typing import List

from test_framework import generic_test


def matrix_search(A: List[List[int]], x: int) -> bool:
    m, n = len(A), len(A[0])
    i, j = 0, n - 1
    while 0 <= i < m and 0 <= j < n:
        current = A[i][j]
        if x > current:
            i += 1
        elif x < current:
            j -= 1
        else:
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_row_col_sorted_matrix.py',
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
