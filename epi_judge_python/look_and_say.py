from test_framework import generic_test
from itertools import groupby


def look_and_say(n: int) -> str:
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(list(value))) + key for key, value in groupby(s))
    return s


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
