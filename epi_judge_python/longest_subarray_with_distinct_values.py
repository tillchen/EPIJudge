from typing import List

from test_framework import generic_test


def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    if not A:
        return 0
    if len(A) == 1:
        return 1
    result = 0
    i, j = 0, 1
    set_of_entries = {A[0]}
    while j < len(A):
        if A[j] not in set_of_entries:
            set_of_entries.add(A[j])
            j += 1
        else:
            set_of_entries.remove(A[i])
            i += 1
        result = max(result, j - i)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
