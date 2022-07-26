from math import prod
from typing import List

from test_framework import generic_test


def calculate_bonus(productivity: List[int]) -> int:
    bonuses = [1] * len(productivity)
    for i in range(1, len(bonuses)):
        if productivity[i] > productivity[i - 1]:
            bonuses[i] = bonuses[i - 1] + 1
    for i in range(len(bonuses) - 2, -1, -1):
        if productivity[i] > productivity[i + 1]:
            bonuses[i] = max(bonuses[i], bonuses[i + 1] + 1)
    return sum(bonuses)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bonus.py', 'bonus.tsv',
                                       calculate_bonus))
