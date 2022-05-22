from test_framework import generic_test


def square_root(k: int) -> int:
    low, high = 0, k
    while low <= high:
        mid = low + (high - low) // 2
        mid_squared = mid * mid
        if mid_squared < k:
            low = mid + 1
        elif mid_squared > k:
            high = mid - 1
        else:
            return mid
    return low - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
