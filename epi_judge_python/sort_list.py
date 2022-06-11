from typing import Optional

from list_node import ListNode
from test_framework import generic_test

def merge_sorted_lists(L1: ListNode, L2: ListNode) -> ListNode:
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


def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    if not L or not L.next:
        return L
    previous_slow, slow, fast = None, L, L
    while fast and fast.next:
        previous_slow = slow
        slow = slow.next
        fast = fast.next.next
    previous_slow.next = None
    return merge_sorted_lists(stable_sort_list(L), stable_sort_list(slow))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
