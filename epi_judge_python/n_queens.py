from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:
    result = []
    current_column_placement = [0] * n
    def helper(row: int):
        if row == n:
            result.append(list(current_column_placement))
            return
        for column in range(n):
            if all(abs(c - column) not in (0, row - i) for i, c in enumerate(current_column_placement[:row])):
                current_column_placement[row] = column
                helper(row + 1)
    helper(0)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
