from functools import partial
from typing import List
from xmlrpc.client import boolean

from test_framework import generic_test

import math

def has_duplicates(block: List[int]) -> boolean:
    block = [x for x in block if x != 0]
    return len(set(block)) != len(block)

# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    n = len(partial_assignment)
    if any(
        has_duplicates([partial_assignment[i][j] for j in range(n)]) or
        has_duplicates([partial_assignment[j][i] for j in range(n)])
        for i in range(n)
    ):
        return False
    region_size = int(math.sqrt(n))
    return all(not has_duplicates([
        partial_assignment[a][b]
        for a in range(region_size * I, region_size * (I + 1))
        for b in range(region_size * J, region_size * (J + 1))
        ]) for I in range(region_size) for J in range(region_size)
    )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
