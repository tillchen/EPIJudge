from typing import List
from math import sqrt

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes_brute_force(n: int) -> List[int]:
    # O(n sqrt(n))
    result = []
    for i in range(2, n + 1):
        if is_prime(i):
            result.append(i)
    return result

def generate_primes(n: int) -> List[int]:
    # O(n log log n)
    result = []
    is_prime_sieve = [False, False] + [True] * (n - 1)
    for i in range(2, n + 1):
        if is_prime_sieve[i]:
            result.append(i)
            for j in range(2 * i, n + 1, i):
                is_prime_sieve[j] = False
    return result

def is_prime(n: int) -> bool:
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
