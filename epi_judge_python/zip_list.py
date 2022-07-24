from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def zipping_linked_list(L: ListNode) -> Optional[ListNode]:
    if not L or not L.next:
        return L
    slow, fast = L, L
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    first_half_head = L
    second_half_head = slow.next
    slow.next = None
    previous, current = None, second_half_head
    while current:
        next_ = current.next
        current.next = previous
        previous = current
        current = next_
    second_half_head = previous
    result = ListNode(next=first_half_head)
    while first_half_head and second_half_head:
        first_half_head_next = first_half_head.next
        first_half_head.next = second_half_head
        first_half_head = first_half_head_next
        second_half_head_next = second_half_head.next
        second_half_head.next = first_half_head
        second_half_head = second_half_head_next
    return result.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('zip_list.py', 'zip_list.tsv',
                                       zipping_linked_list))
