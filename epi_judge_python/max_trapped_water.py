from typing import List

from test_framework import generic_test


def get_max_trapped_water(heights: List[int]) -> int:
    i, j = 0, len(heights) - 1
    result = 0
    while i < j:
        result = max(result, (j - i) * min(heights[i], heights[j]))
        if heights[i] < heights[j]:
            i += 1
        else:
            j -= 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_trapped_water.py',
                                       'max_trapped_water.tsv',
                                       get_max_trapped_water))
