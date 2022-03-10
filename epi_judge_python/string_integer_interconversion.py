from test_framework import generic_test
from test_framework.test_failure import TestFailure

from collections import deque

def int_to_string(x: int) -> str:
    is_negative = x < 0
    x = abs(x)
    result = deque()
    while x:
        result.appendleft(str(x % 10))
        x //= 10
    if is_negative:
        result.appendleft('-')
    return ''.join(result) if result else '0'


def string_to_int(s: str) -> int:
    is_negative = False
    if s[0] == '-':
        is_negative = True
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    result = 0
    for i, c in enumerate(s[::-1]):
        result += int(c) * 10 ** i
    return result if not is_negative else -result


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
