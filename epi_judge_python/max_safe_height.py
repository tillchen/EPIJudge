from test_framework import generic_test


def get_height(cases: int, drops: int) -> int:
    memo = {}
    def helper(cases: int, drops: int) -> int:
        if cases == 0 or drops == 0:
            return 0
        if cases == 1:
            return drops
        if (cases, drops) not in memo:
            memo[(cases, drops)] = helper(cases - 1, drops - 1) + 1 + helper(cases, drops - 1)
        return memo[(cases, drops)]
    return helper(cases, drops)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_safe_height.py',
                                       'max_safe_height.tsv', get_height))
