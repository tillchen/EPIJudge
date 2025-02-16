import functools
from typing import Optional

from posting_list_node import PostingListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def copy_postings_list_0(L: PostingListNode) -> Optional[PostingListNode]:
    if not L:
        return None
    original_to_copy = {}
    current = L
    while current:
        copy = PostingListNode(current.order, None)
        original_to_copy[current] = copy
        current = current.next
    current = L
    while current:
        original_to_copy[current].next = original_to_copy[current.next] if current.next in original_to_copy else None
        original_to_copy[current].jump = original_to_copy[current.jump] if current.jump in original_to_copy else None
        current = current.next
    return original_to_copy[L]


def copy_postings_list(L: PostingListNode) -> Optional[PostingListNode]:
    if not L:
        return None
    # Step 1: Copy and cross reference.
    current = L
    while current:
        copy = PostingListNode(current.order, current.next)
        current.next = copy
        current = copy.next
    # Step 2: Assign the jump field.
    current = L
    while current:
        if current.jump:
            current.next.jump = current.jump.next
        current = current.next.next
    # Step 3: Restore the list.
    current = L
    result = L.next
    while current.next:
        current.next, current = current.next.next, current.next
    return result

def assert_lists_equal(orig, copy):
    node_mapping = dict()
    o_it = orig
    c_it = copy
    while o_it:
        if not c_it:
            raise TestFailure('Copied list has fewer nodes than the original')
        if o_it.order != c_it.order:
            raise TestFailure('Order value mismatch')
        node_mapping[o_it] = c_it
        o_it = o_it.next
        c_it = c_it.next

    if c_it:
        raise TestFailure('Copied list has more nodes than the original')

    o_it = orig
    c_it = copy
    while o_it:
        if c_it in node_mapping:
            raise TestFailure(
                'Copied list contains a node from the original list')
        if o_it.jump is None:
            if c_it.jump is not None:
                raise TestFailure(
                    'Jump link points to a different nodes in the copied list')
        else:
            if not node_mapping[o_it.jump] is c_it.jump:
                raise TestFailure(
                    'Jump link points to a different nodes in the copied list')
        o_it = o_it.next
        c_it = c_it.next


@enable_executor_hook
def copy_postings_list_wrapper(executor, l):
    def create_posting_list(serialized):
        key_mapping = dict()
        head = None
        for (order, _) in reversed(serialized):
            head = PostingListNode(order, head)
            key_mapping[order] = head

        list_it = head
        for (_, jump_index) in serialized:
            if jump_index != -1:
                list_it.jump = key_mapping.get(jump_index, None)
                if not list_it.jump:
                    raise RuntimeError('Jump index out of range')

        return head

    head = create_posting_list(l)

    copy = executor.run(functools.partial(copy_postings_list, head))

    assert_lists_equal(head, copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('copy_posting_list.py',
                                       'copy_posting_list.tsv',
                                       copy_postings_list_wrapper))
