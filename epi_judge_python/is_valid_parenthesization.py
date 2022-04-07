from test_framework import generic_test
from collections import deque


def is_well_formed(s: str) -> bool:
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    stack = deque()
    for c in s:
        if c in pairs:
            stack.append(c)
        else:
            if not stack or pairs[stack.pop()] != c:
                return False
    return not stack


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
