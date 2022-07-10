from test_framework import generic_test


def change_making(cents: int) -> int:
    coins = [100, 50, 25, 10, 5, 1]
    result = 0
    for coin in coins:
        result += cents // coin
        cents %= coin
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('making_change.py', 'making_change.tsv',
                                       change_making))
