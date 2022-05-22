from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    low, high, result = 0, len(A) - 1, -1
    while low <= high:
        mid = low + (high - low) // 2
        if k > A[mid]:
            low = mid + 1
        elif k < A[mid]:
            high = mid - 1
        else:
            result = mid
            high = mid - 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
