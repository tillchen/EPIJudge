import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists_0(l0: ListNode, l1: ListNode) -> ListNode:
    set_of_nodes = set()
    while l0:
        set_of_nodes.add(l0)
        l0 = l0.next
    while l1:
        if l1 in set_of_nodes:
            return l1
        l1 = l1.next
    return None

def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    def get_list_length(l: ListNode) -> int:
        result = 0
        while l:
            result += 1
            l = l.next
        return result
    len_l0 = get_list_length(l0)
    len_l1 = get_list_length(l1)
    # Make l1 the longer list
    if len_l0 > len_l1:
        l0, l1 = l1, l0
    for _ in range(abs(len_l0 - len_l1)):
        l1 = l1.next
    while l0 and l1 and l0 is not l1:
        l0 = l0.next
        l1 = l1.next
    return l0


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
