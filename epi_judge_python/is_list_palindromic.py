from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome_0(L: ListNode) -> bool:
    my_L = []
    while L:
        my_L.append(L.data)
        L = L.next
    return my_L == my_L[::-1]

def reverse_linked_list(L: ListNode) -> ListNode:
    previous, current = None, L
    while current:
        next_ = current.next
        current.next = previous
        previous = current
        current = next_
    return previous

def is_linked_list_a_palindrome(L: ListNode) -> bool:
    slow, fast = L, L
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    first_half, second_half = L, reverse_linked_list(slow)
    while first_half and second_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
