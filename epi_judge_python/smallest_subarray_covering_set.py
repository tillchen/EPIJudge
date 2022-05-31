import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph: List[str], keywords: Set[str]) -> Subarray:
    keywords_to_indices = {}
    min_length = float('inf')
    result = Subarray(0, 0)
    for i, keyword in enumerate(paragraph):
        if keyword in keywords:
            keywords_to_indices[keyword] = i
            if keywords_to_indices.keys() == keywords and (new_min_length := i - min(keywords_to_indices.values()) + 1) < min_length:
                min_length = new_min_length
                result = Subarray(min(keywords_to_indices.values()), i)
    return result

@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
