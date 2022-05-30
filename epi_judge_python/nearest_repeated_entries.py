from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    words_to_indices = {}
    result = float('inf')
    for i, word in enumerate(paragraph):
        if word in words_to_indices:
            result = min(result, i - words_to_indices[word])
        words_to_indices[word] = i
    return result if result != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
