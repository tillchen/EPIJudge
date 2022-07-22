import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def rotate_array_0(rotate_amount: int, A: List[int]) -> None:
    result = [0] * len(A)
    for i in range(len(A)):
        result[(i + rotate_amount) % len(A)] = A[i]
    A[:] = result

def rotate_array_1(rotate_amount: int, A: List[int]) -> None:
    rotate_amount %= len(A)
    A[:] = A[::-1]
    A[:rotate_amount] = A[:rotate_amount][::-1]
    A[rotate_amount:] = A[rotate_amount:][::-1]

def rotate_array(rotate_amount: int, A: List[int]) -> None:
    rotate_amount %= len(A)
    def reverse(i: int, j: int):
        while i < j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
    reverse(0, len(A) - 1)
    reverse(0, rotate_amount - 1)
    reverse(rotate_amount, len(A) - 1)

@enable_executor_hook
def rotate_array_wrapper(executor, A, rotate_amount):
    a_copy = A[:]
    executor.run(functools.partial(rotate_array, rotate_amount, a_copy))
    return a_copy


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rotate_array.py', 'rotate_array.tsv',
                                       rotate_array_wrapper))
