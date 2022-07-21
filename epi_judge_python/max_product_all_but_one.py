from typing import List

from test_framework import generic_test
from operator import mul
from functools import reduce

def find_biggest_n_minus_one_product(A: List[int]) -> int:
    result = 0
    for i in range(len(A)):
        result = max(result, reduce(mul, A[:i] + A[i+1:], 1))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_product_all_but_one.py',
                                       'max_product_all_but_one.tsv',
                                       find_biggest_n_minus_one_product))
