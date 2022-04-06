import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def list_pivoting(l: ListNode, x: int) -> Optional[ListNode]:
    smaller_head = smaller_iter = ListNode()
    equal_head = equal_iter = ListNode()
    larger_head = larger_iter = ListNode()
    while l:
        if l.data < x:
            smaller_iter.next = l
            smaller_iter = smaller_iter.next
        elif l.data == x:
            equal_iter.next = l
            equal_iter = equal_iter.next
        else:
            larger_iter.next = l
            larger_iter = larger_iter.next
        l = l.next

    larger_iter.next = None
    equal_iter.next = larger_head.next
    smaller_iter.next = equal_head.next
    return smaller_head.next


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pivot_list.py', 'pivot_list.tsv',
                                       list_pivoting_wrapper))
