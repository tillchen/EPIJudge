from test_framework import generic_test
from collections import deque


def evaluate(expression: str) -> int:
    stack = deque()
    symbols = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: x // y
    }
    for c in expression.split(','):
        if c not in symbols:
            stack.append(int(c))
        else:
            stack.append(symbols[c](stack.pop(), stack.pop()))
    return stack[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
