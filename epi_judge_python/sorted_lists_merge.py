from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(
    L1: Optional[ListNode],
    L2: Optional[ListNode]
) -> Optional[ListNode]:
    result = current = ListNode()
    while L1 and L2:
        if L1.data < L2.data:
            current.next = L1
            L1 = L1.next
        else:
            current.next = L2
            L2 = L2.next
        current = current.next
    current.next = L1 if L1 else L2
    return result.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
