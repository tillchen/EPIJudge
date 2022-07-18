from typing import List

from test_framework import generic_test

from collections import deque

def fill_surrounded_regions(board: List[List[str]]) -> None:
    m, n = len(board), len(board[0])
    queue = deque([(i, j) for k in range(m) for i, j in ((k, 0), (k, n - 1))] + [(i, j) for k in range(n) for i, j in ((0, k), (m - 1, k))])
    while queue:
        x, y = queue.popleft()
        if 0 <= x < m and 0 <= y < n and board[x][y] == 'W':
            board[x][y] = 'T'
            queue.extend([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])
    board[:] = [['W' if c == 'T' else 'B' for c in row] for row in board]


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
