from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L:
        return L
    even_head, odd_head = L, L.next
    even_current, odd_current = even_head, odd_head
    while even_current and odd_current and even_current.next and odd_current.next:
        even_current.next = odd_current.next
        even_current = even_current.next
        odd_current.next = even_current.next
        odd_current = odd_current.next
    even_current.next = odd_head
    return even_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
