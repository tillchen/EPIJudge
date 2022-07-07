from typing import List

from test_framework import generic_test


def minimum_path_weight(triangle: List[List[int]]) -> int:
    memo = {}
    def helper(i: int, j: int) -> int:
        if i == len(triangle):
            return 0
        if j == i + 1:
            return 0
        if (i, j) not in memo:
            memo[(i, j)] = triangle[i][j] + min(helper(i + 1, j), helper(i + 1, j + 1))
        return memo[(i, j)]
    return helper(0, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_weight_path_in_a_triangle.py',
            'minimum_weight_path_in_a_triangle.tsv', minimum_path_weight))
