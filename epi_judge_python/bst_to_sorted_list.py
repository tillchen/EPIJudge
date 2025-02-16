import functools
from typing import Optional

from bst_node import BstNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from collections import namedtuple


def bst_to_doubly_linked_list_0(tree: BstNode) -> Optional[BstNode]:
    if not tree:
        return None
    dummy = previous = BstNode()
    def inorder_traversal(node: BstNode):
        if not node:
            return
        inorder_traversal(node.left)
        current = BstNode(node.data)
        nonlocal previous
        previous.right = current
        current.left = previous
        previous = current
        inorder_traversal(node.right)
    inorder_traversal(tree)
    result = dummy.right
    result.left = None
    return result

def bst_to_doubly_linked_list(tree: BstNode) -> Optional[BstNode]:
    HeadAndTail = namedtuple('HeadAndTail', ('head', 'tail'))
    def helper(tree: BstNode) -> HeadAndTail:
        if not tree:
            return HeadAndTail(None, None)
        left, right = helper(tree.left), helper(tree.right)
        if left.tail:
            left.tail.right = tree
        tree.left = left.tail
        tree.right = right.head
        if right.head:
            right.head.left = tree
        return HeadAndTail(left.head or tree, right.tail or tree)
    return helper(tree).head


@enable_executor_hook
def bst_to_doubly_linked_list_wrapper(executor, tree):
    l = executor.run(functools.partial(bst_to_doubly_linked_list, tree))

    if l is not None and l.left is not None:
        raise TestFailure(
            'Function must return the head of the list. Left link must be None'
        )

    v = []
    while l:
        v.append(l.data)
        if l.right and l.right.left is not l:
            raise TestFailure('List is ill-formed')
        l = l.right

    return v


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_to_sorted_list.py',
                                       'bst_to_sorted_list.tsv',
                                       bst_to_doubly_linked_list_wrapper))
