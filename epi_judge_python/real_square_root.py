from test_framework import generic_test
import math


def square_root(x: float) -> float:
    low, high = (1.0, x) if x > 1.0 else (x, 1.0)
    while not math.isclose(low, high):
        mid = (low + high) / 2
        mid_squared = mid * mid
        if mid_squared > x:
            high = mid
        else:
            low = mid
    return low


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
