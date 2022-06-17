from typing import List

from test_framework import generic_test
import math
import bintrees

class ABSqrt2:
    def __init__(self, a: int, b: int) -> None:
        self.a, self.b = a, b
        self.val = a + b * math.sqrt(2)

    def __lt__(self, other: object) -> bool:
        return self.val < other.val

    def __eq__(self, other: object) -> bool:
        return self.val == other.val


def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    candidates = bintrees.RBTree()
    candidates.insert(ABSqrt2(0, 0), None)
    result = []
    while len(result) < k:
        current = candidates.pop_min()[0]
        result.append(current.val)
        candidates.insert(ABSqrt2(current.a + 1, current.b), None)
        candidates.insert(ABSqrt2(current.a, current.b + 1), None)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('a_b_sqrt2.py', 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
