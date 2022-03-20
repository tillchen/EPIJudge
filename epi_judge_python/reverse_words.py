import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

from typing import List


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s: List[str]):
    if not s:
        return []
    s[:] = ''.join(s).split(' ')[::-1]
    result = []
    for x in s:
        result += list(x) + [' ']
    del result[-1]
    s[:] = result


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
