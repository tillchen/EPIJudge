from typing import List
from math import inf
from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    result = 0
    current_min = inf
    for price in prices:
        current_min = min(current_min, price)
        result = max(result, price - current_min)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
