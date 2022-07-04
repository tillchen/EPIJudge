from test_framework import generic_test
from functools import lru_cache

@lru_cache
def number_of_ways(n: int, m: int) -> int:
    if n == 1 or m == 1:
        return 1
    return number_of_ways(n - 1, m) + number_of_ways(n, m - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
