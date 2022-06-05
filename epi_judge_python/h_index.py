from typing import List

from test_framework import generic_test


def h_index(citations: List[int]) -> int:
    for i, citation in enumerate(sorted(citations, reverse=True)):
        if i + 1 > citation:
            return i
    return len(citations)


if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
