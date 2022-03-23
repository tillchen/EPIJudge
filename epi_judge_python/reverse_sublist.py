from multiprocessing import cpu_count
from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if not L or start == finish:
        return L
    connection_left, current = ListNode(), L
    connection_left.next = L
    for _ in range(start - 1):
        connection_left = current
        current = current.next
    for _ in range(finish - start):
        current = current.next
        connection_right = current.next
    previous, current = None, connection_left.next
    while current is not connection_right:
        next = current.next
        current.next = previous
        previous = current
        current = next
    if connection_left.next:
        connection_left.next.next = connection_right
    connection_left.next = previous
    return L if start != 1 else previous


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
