import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# a -> dd, remove b
def replace_and_remove(size: int, s: List[str]) -> int:
    # First pass, remove 'b's and count 'a's.
    write_index, a_count = 0, 0
    for i, c in enumerate(s[:size]):
        if c == 'a':
            a_count += 1
        if c != 'b':
            s[write_index] = s[i]
            write_index += 1
    # Second pass, a -> dd from the back.
    total_size = write_index + a_count
    current_index = write_index - 1
    write_index = total_size - 1
    while current_index > -1:
        if s[current_index] == 'a':
            s[write_index - 1] = s[write_index] = 'd'
            write_index -= 2
        else:
            s[write_index] = s[current_index]
            write_index -= 1
        current_index -= 1
    return total_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
