from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import deque

def preorder_traversal(tree: BinaryTreeNode) -> List[int]:
    stack = deque()
    result = []
    while stack or tree:
        if tree:
            result.append(tree.data)
            stack.append(tree)
            tree = tree.left
        else:
            tree = stack.pop()
            tree = tree.right
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_preorder.py', 'tree_preorder.tsv',
                                       preorder_traversal))
