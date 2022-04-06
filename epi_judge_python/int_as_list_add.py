from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    head = current = ListNode()
    is_carry_over = False
    while L1 or L2 or is_carry_over:
        current_value = (L1.data if L1 else 0) + (L2.data if L2 else 0)
        if is_carry_over:
            current_value += 1
        is_carry_over = True if current_value > 9 else False
        current_value %= 10
        current.next = ListNode(current_value)
        current = current.next
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None
    return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
