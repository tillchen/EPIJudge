from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import deque

def inorder_traversal_0(tree: BinaryTreeNode) -> List[int]:
    result = []
    def helper(tree: BinaryTreeNode, path: List[int]) -> None:
        if not tree:
            return
        helper(tree.left, path)
        path.append(tree.data)
        helper(tree.right, path)

    helper(tree, result)
    return result

def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    stack = deque()
    result = []
    while stack or tree:
        if tree:
            stack.append(tree)
            tree = tree.left
        else:
            tree = stack.pop()
            result.append(tree.data)
            tree = tree.right
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
