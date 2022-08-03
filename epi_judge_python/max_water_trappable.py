from typing import List

from test_framework import generic_test


def calculate_trapping_water(heights: List[int]) -> int:
    max_height_index = heights.index(max(heights))
    def trap_water_until_the_end(heights: List[int]) -> int:
        current_max = -float('inf')
        result = 0
        for height in heights:
            if height >= current_max:
                current_max = height
            else:
                result += current_max - height
        return result

    return trap_water_until_the_end(heights[:max_height_index + 1]) + trap_water_until_the_end(heights[-1:max_height_index:-1])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_water_trappable.py',
                                       'max_water_trappable.tsv',
                                       calculate_trapping_water))
