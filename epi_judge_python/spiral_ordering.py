from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    spiral_ordering = []

    def matrix_layer_in_clockwise(offset: int):
        if offset == len(square_matrix) - offset - 1:
            # Center of the odd dimension.
            spiral_ordering.append(square_matrix[offset][offset])
            return
        spiral_ordering.extend(square_matrix[offset][offset: -1 - offset])
        spiral_ordering.extend(list(zip(*square_matrix))[-1 - offset][offset: -1 - offset])
        spiral_ordering.extend(square_matrix[-1 - offset][-1 -offset: offset: -1])
        spiral_ordering.extend(list(zip(*square_matrix))[offset][-1 -offset: offset: -1])

    for offset in range((len(square_matrix) + 1) // 2):
        matrix_layer_in_clockwise(offset)

    return spiral_ordering

def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    SHIFT = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = x = y = 0
    spiral_ordering = []

    for _ in range(len(square_matrix) ** 2):
        spiral_ordering.append(square_matrix[x][y])
        square_matrix[x][y] = 0
        next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        if (next_x not in range(len(square_matrix)) or
            next_y not in range(len(square_matrix)) or
            square_matrix[next_x][next_y] == 0
        ):
            direction = (direction + 1) % 4
            next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        x, y = next_x, next_y
    return spiral_ordering

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
