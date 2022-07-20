from typing import List

from test_framework import generic_test


def find_first_missing_positive_0(A: List[int]) -> int:
    A = [x for x in sorted(set(A)) if x > 0]
    result = 1
    for x in A:
        if x != result:
            return result
        result += 1
    return result

def find_first_missing_positive(A: List[int]) -> int:
    set_of_A = set(A)
    result = 1
    while result in set_of_A:
        result += 1
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('first_missing_positive_entry.py',
                                       'first_missing_positive_entry.tsv',
                                       find_first_missing_positive))
