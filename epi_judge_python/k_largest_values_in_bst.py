from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst_0(tree: BstNode, k: int) -> List[int]:
    inorder_path = []
    def inorder_traversal(tree: BstNode):
        if not tree:
            return
        inorder_traversal(tree.left)
        inorder_path.append(tree.data)
        inorder_traversal(tree.right)
    inorder_traversal(tree)
    return inorder_path[-k:]

def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    result = []
    def reverse_inorder_traversal(tree: BstNode):
        if not tree or len(result) >= k:
            return
        reverse_inorder_traversal(tree.right)
        if len(result) >= k:
            return
        result.append(tree.data)
        reverse_inorder_traversal(tree.left)
    reverse_inorder_traversal(tree)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
