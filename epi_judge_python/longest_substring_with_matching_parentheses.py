from test_framework import generic_test
from collections import deque


def longest_matching_parentheses(s: str) -> int:
    stack = deque([-1])
    result = 0
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                result = max(result, i - stack[-1])
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_substring_with_matching_parentheses.py',
            'longest_substring_with_matching_parentheses.tsv',
            longest_matching_parentheses))
