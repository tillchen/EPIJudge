from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import deque

def preorder_traversal(tree: BinaryTreeNode) -> List[int]:
    stack = deque()
    stack.append(tree)
    result = []
    while stack:
        current = stack.pop()
        if current:
            result.append(current.data)
            stack.append(current.right)
            stack.append(current.left)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_preorder.py', 'tree_preorder.tsv',
                                       preorder_traversal))
