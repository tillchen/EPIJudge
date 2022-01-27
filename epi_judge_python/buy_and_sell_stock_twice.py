from typing import List
from math import inf

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    # Profits if sell on or before day i.
    first_transaction_profits = []
    current_min = inf
    profit = 0
    for price in prices:
        current_min = min(current_min, price)
        profit = max(profit, price - current_min)
        first_transaction_profits.append(profit)
    total_profits = [0] * len(prices)
    current_max = -inf
    profit = 0
    for i, price in reversed(list(enumerate(prices[1:], start=1))):
        current_max = max(current_max, price)
        # Profit if buy on or after day i.
        profit = max(profit, current_max - price)
        total_profits[i] = first_transaction_profits[i] + profit
    return max(total_profits)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
