from typing import Iterator, List

from test_framework import generic_test, test_utils
from collections import defaultdict
from itertools import tee
from collections import Counter

# Finds the candidates which may occur > n / k times.
def search_frequent_items_0(k: int, stream: Iterator[str]) -> List[str]:
    x_to_frequency = defaultdict(int)
    for x in stream:
        x_to_frequency[x] += 1
    return [x for x, frequency in x_to_frequency.items() if frequency > sum(x_to_frequency.values()) / k]

def search_frequent_items(k: int, stream: Iterator[str]) -> List[str]:
    stream, stream_copy = tee(stream)
    x_to_frequency = Counter()
    n = 0
    for x in stream:
        n += 1
        x_to_frequency[x] += 1
        if len(x_to_frequency) == k:
            for key in x_to_frequency:
                x_to_frequency[key] -= 1
            x_to_frequency = +x_to_frequency
    for x in x_to_frequency:
        x_to_frequency[x] = 0
    for x in stream_copy:
        if x in x_to_frequency:
            x_to_frequency[x] += 1
    return [x for x, frequency in x_to_frequency.items() if frequency > n / k]


def search_frequent_items_wrapper(k, stream):
    return search_frequent_items(k, iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_frequent_items.py',
                                       'search_frequent_items.tsv',
                                       search_frequent_items_wrapper,
                                       test_utils.unordered_compare))
