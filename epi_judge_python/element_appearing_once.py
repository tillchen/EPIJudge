from typing import List

from test_framework import generic_test
from collections import Counter

def find_element_appears_once(A: List[int]) -> int:
    return Counter(A).most_common()[:-2:-1][0][0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('element_appearing_once.py',
                                       'element_appearing_once.tsv',
                                       find_element_appears_once))
