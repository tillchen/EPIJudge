from typing import List

from test_framework import generic_test


# [[1,2,3],[4,5,6],[7,8,9]] -> [[7,4,1],[8,5,2],[9,6,3]]
def rotate_matrix_0(square_matrix: List[List[int]]) -> None:
    square_matrix[:] = list(map(list, zip(*square_matrix)))
    square_matrix[:] = [row[::-1] for row in square_matrix]

def rotate_matrix(square_matrix: List[List[int]]) -> None:
    n = len(square_matrix)
    for i in range(n // 2):
        for j in range(i, n - 1 - i):
            square_matrix[i][j], square_matrix[~j][i], square_matrix[~i][~j], square_matrix[j][~i] = (square_matrix[~j][i],
            square_matrix[~i][~j], square_matrix[j][~i], square_matrix[i][j])


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
