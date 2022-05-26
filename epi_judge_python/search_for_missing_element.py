import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    set_of_numbers = set()
    duplicate = 0
    for x in A:
        if x in set_of_numbers:
            duplicate = x
            break
        set_of_numbers.add(x)
    n = len(A)
    expected_sum = (n - 1) * n / 2
    actual_sum = sum(A)
    missing = duplicate + (expected_sum - actual_sum)
    return DuplicateAndMissing(duplicate, missing)


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    return fmt(value) if prop in (PropertyName.EXPECTED,
                                  PropertyName.RESULT) else value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_missing_element.py',
                                       'find_missing_and_duplicate.tsv',
                                       find_duplicate_missing,
                                       res_printer=res_printer))
