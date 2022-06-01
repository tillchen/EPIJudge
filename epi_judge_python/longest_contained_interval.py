from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    unprocessed_set = set(A)
    result = 0
    for x in A:
        if x in unprocessed_set:
            local_range = 1
            unprocessed_set.remove(x)
            current = x
            while current - 1 in unprocessed_set:
                current -= 1
                unprocessed_set.remove(current)
                local_range += 1
            current = x
            while current + 1 in unprocessed_set:
                current += 1
                unprocessed_set.remove(current)
                local_range += 1
            result = max(result, local_range)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
