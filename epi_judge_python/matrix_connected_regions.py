from typing import List

from test_framework import generic_test


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    def helper(x: int, y: int, b: bool):
        if not 0 <= x < len(image) or not 0 <= y < len(image[0]) or image[x][y] is not b:
            return
        image[x][y] = not b
        helper(x - 1, y, b)
        helper(x + 1, y, b)
        helper(x, y - 1, b)
        helper(x, y + 1, b)
    helper(x, y, image[x][y])


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
