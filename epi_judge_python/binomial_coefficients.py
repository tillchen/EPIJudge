from test_framework import generic_test


def compute_binomial_coefficient(n: int, k: int) -> int:
    memo = [[-1] * (k + 1) for _ in range(n + 1)]
    def helper(n: int, k: int) -> int:
        if memo[n][k] == -1:
            if k == 0 or n == k:
                memo[n][k] = 1
            else:
                memo[n][k] = helper(n - 1, k) + helper(n - 1, k - 1)
        return memo[n][k]
    return helper(n, k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('binomial_coefficients.py',
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
