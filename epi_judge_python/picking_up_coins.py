from typing import List

from test_framework import generic_test


def maximum_revenue(coins: List[int]) -> int:
    memo = {}
    def helper(i: int, j:int) -> int:
        if (i, j) not in memo:
            if i > j:
                return 0
            max_1 = coins[i] + min(helper(i + 2, j), helper(i + 1, j - 1))
            max_2 = coins[j] + min(helper(i + 1, j - 1), helper(i, j - 2))
            memo[(i, j)] = max(max_1, max_2)
        return memo[(i, j)]
    return helper(0, len(coins) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('picking_up_coins.py',
                                       'picking_up_coins.tsv',
                                       maximum_revenue))
