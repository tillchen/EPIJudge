import collections
from typing import List

from bst_node import BstNode
from test_framework import generic_test

Interval = collections.namedtuple('Interval', ('left', 'right'))


def range_lookup_in_bst_0(tree: BstNode, interval: Interval) -> List[int]:
    result = []
    def inorder_traversal(tree: BstNode):
        if not tree:
            return
        inorder_traversal(tree.left)
        if interval.left <= tree.data <= interval.right:
            result.append(tree.data)
        inorder_traversal(tree.right)
    inorder_traversal(tree)
    return result

def range_lookup_in_bst(tree: BstNode, interval: Interval) -> List[int]:
    result = []
    def helper(tree: BstNode):
        if not tree:
            return
        if interval.left <= tree.data <= interval.right:
            helper(tree.left)
            result.append(tree.data)
            helper(tree.right)
        elif tree.data < interval.left:
            helper(tree.right)
        else:
            helper(tree.left)
    helper(tree)
    return result


def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('range_lookup_in_bst.py',
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))
