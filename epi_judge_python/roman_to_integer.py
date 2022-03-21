from test_framework import generic_test
from functools import reduce


def roman_to_integer_0(s: str) -> int:
    mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = sum(mapping[c] for c in s)
    for i, c in enumerate(s):
        if i + 1 < len(s):
            next_c = s[i + 1]
            if (c == 'I' and next_c in 'VX') or (c == 'X' and next_c in 'LC') or (c == 'C' and next_c in 'DM'):
                result -= 2 * mapping[c]
    return result

def roman_to_integer(s: str) -> int:
    mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    return reduce(lambda x, i: x  + (-mapping[s[i]] if mapping[s[i]] < mapping[s[i + 1]] else mapping[s[i]]), reversed(range(len(s) - 1)), mapping[s[-1]])

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
