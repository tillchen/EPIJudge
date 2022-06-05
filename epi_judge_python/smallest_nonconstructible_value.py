from typing import List

from test_framework import generic_test


def smallest_nonconstructible_value(A: List[int]) -> int:
    max_constructible_value = 0
    for x in sorted(A):
        if x > max_constructible_value + 1:
            break
        max_constructible_value += x
    return max_constructible_value + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('smallest_nonconstructible_value.py',
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
