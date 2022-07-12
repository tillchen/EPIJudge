from typing import Iterator

from test_framework import generic_test
from collections import Counter

def majority_search(stream: Iterator[str]) -> str:
    return Counter(stream).most_common(1)[0][0]


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('majority_element.py',
                                       'majority_element.tsv',
                                       majority_search_wrapper))
