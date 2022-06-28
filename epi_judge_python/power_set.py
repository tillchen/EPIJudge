from typing import List

from test_framework import generic_test, test_utils

import itertools
from itertools import combinations

def generate_power_set_0(input_set: List[int]) -> List[List[int]]:
    return list(itertools.chain.from_iterable(map(list, combinations(input_set, x)) for x in range(len(input_set) + 1)))

def generate_power_set(input_set: List[int]) -> List[List[int]]:
    result = []
    def helper(to_be_selected: int, selected_so_far: List[int]):
        if to_be_selected == len(input_set):
            result.append(list(selected_so_far))
            return
        helper(to_be_selected + 1, selected_so_far)
        helper(to_be_selected + 1, selected_so_far + [input_set[to_be_selected]])

    helper(0, [])
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
