from typing import List, Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last_0(L: ListNode, k: int) -> Optional[ListNode]:
    def get_length(L: ListNode) -> int:
        result = 0
        while L:
            L = L.next
            result += 1
        return result

    l_len = get_length(L)
    if k == l_len:
        return L.next

    result = L
    for _ in range(l_len - k - 1):
        L = L.next

    L.next = L.next.next if L.next else None
    return result


def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    first = L
    for _ in range(k):
        first = first.next
    head = ListNode(next=L)
    second = head
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next if second.next else None
    return head.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
