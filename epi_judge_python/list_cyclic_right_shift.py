from typing import Optional
from typing import Tuple

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    def get_list_length_and_last_node(L: ListNode) -> Tuple[int, ListNode]:
        result = 0
        previous = None
        while L:
            previous = L
            L = L.next
            result += 1
        return result, previous

    if not L or k == 0:
        return L

    l_len, last_node = get_list_length_and_last_node(L)
    k %= l_len
    target_index = l_len - k - 1
    current = L
    for _ in range(target_index):
        current = current.next
    last_node.next = L
    head = current.next
    current.next = None
    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
