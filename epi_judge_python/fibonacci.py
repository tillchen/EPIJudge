from test_framework import generic_test
from functools import lru_cache

@lru_cache
def fibonacci_0(n: int) -> int:
    if n < 2:
        return n
    return fibonacci_0(n - 1) + fibonacci_0(n - 2)


memo = {
    0: 0,
    1: 1
}

def fibonacci_1(n: int) -> int:
    if n not in memo:
        memo[n] = fibonacci_1(n - 1) + fibonacci_1(n - 2)
    return memo[n]

def fibonacci_2(n: int) -> int:
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]

def fibonacci(n: int) -> int:
    if n < 2:
        return n
    previous, current = 0, 1
    for _ in range(2, n + 1):
        next = previous + current
        previous = current
        current = next
    return next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
