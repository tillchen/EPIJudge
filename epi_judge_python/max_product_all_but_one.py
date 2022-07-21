from typing import List

from test_framework import generic_test
from operator import mul
from functools import reduce
from itertools import accumulate

def find_biggest_n_minus_one_product_0(A: List[int]) -> int:
    result = 0
    for i in range(len(A)):
        result = max(result, reduce(mul, A[:i] + A[i+1:], 1))
    return result

def find_biggest_n_minus_one_product_1(A: List[int]) -> int:
    products = [1] * len(A)
    products_in_reverse = [1] * len(A)
    current = 1
    for i, x in enumerate(A):
        current *= x
        products[i] = current
    current = 1
    for i in range(len(A) - 1, -1, -1):
        current *= A[i]
        products_in_reverse[i] = current
    result = 0
    for i in range(len(A)):
        prefix = products[i - 1] if i - 1 >= 0 else 1
        suffix = products_in_reverse[i + 1] if i + 1 < len(A) else 1
        result = max(result, prefix * suffix)
    return result

def find_biggest_n_minus_one_product_2(A: List[int]) -> int:
    suffix_products = list(reversed(list(accumulate(reversed(A), mul))))
    prefix_product = 1
    result = 0
    for i in range(len(A)):
        suffix_product = suffix_products[i + 1] if i + 1 < len(A) else 1
        result = max(result, prefix_product * suffix_product)
        prefix_product *= A[i]
    return result

def find_biggest_n_minus_one_product(A: List[int]) -> int:
    num_of_negatives = 0
    least_nonnegative_index, greatest_negative_index, least_negative_index = None, None, None
    for i, x in enumerate(A):
        if x < 0:
            num_of_negatives += 1
            if greatest_negative_index is None or x > A[greatest_negative_index]:
                greatest_negative_index = i
            if least_negative_index is None or x < A[least_negative_index]:
                least_negative_index = i
        else:
            if least_nonnegative_index is None or x < A[least_nonnegative_index]:
                least_nonnegative_index = i
    if num_of_negatives % 2 == 1:
        index_to_skip = greatest_negative_index
    else:
        if least_nonnegative_index is not None:
            index_to_skip = least_nonnegative_index
        else:
            index_to_skip = least_negative_index
    return reduce(mul, (x for i, x in enumerate(A) if i != index_to_skip), 1)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_product_all_but_one.py',
                                       'max_product_all_but_one.tsv',
                                       find_biggest_n_minus_one_product))
