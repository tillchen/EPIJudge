from typing import List

from test_framework import generic_test


def is_pattern_contained_in_grid(grid: List[List[int]], pattern: List[int]) -> bool:
    memo = set()
    def helper(x: int, y: int, offset: int) -> bool:
        if offset == len(pattern):
            return True
        if (
            0 <= x < len(grid) and 0 <= y < len(grid[0])
            and grid[x][y] == pattern[offset]
            and (x, y, offset) not in memo
            and any(helper(x + a, y + b, offset + 1) for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        ):
            return True
        memo.add((x, y, offset))
        return False
    return any(helper(i, j, 0) for i in range(len(grid)) for j in range(len(grid[0])))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
