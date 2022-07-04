from test_framework import generic_test
from functools import lru_cache

@lru_cache
def number_of_ways_0(n: int, m: int) -> int:
    if n == 1 or m == 1:
        return 1
    return number_of_ways_0(n - 1, m) + number_of_ways_0(n, m - 1)

def number_of_ways(n: int, m: int) -> int:
    memo = [[-1] * m for _ in range(n)]
    def helper(n: int, m: int) -> int:
        if memo[n][m] == -1:
            if n == 0 or m == 0:
                memo[n][m] = 1
            else:
                memo[n][m] = helper(n - 1, m) + helper(n, m - 1)
        return memo[n][m]
    return helper(n - 1, m - 1)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
