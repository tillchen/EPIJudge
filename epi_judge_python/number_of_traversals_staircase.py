from test_framework import generic_test

def number_of_ways_to_top(top: int, maximum_step: int) -> int:
    memo = {}
    def helper(top: int) -> int:
        if top < 2:
            return 1
        if top not in memo:
            memo[top] = sum(helper(top - i) for i in range(1, min(top, maximum_step) + 1))
        return memo[top]
    return helper(top)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_staircase.py',
                                       'number_of_traversals_staircase.tsv',
                                       number_of_ways_to_top))
