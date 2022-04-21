import enum
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder_0(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    if not inorder:
        return
    root_val = preorder.pop(0)
    root = BinaryTreeNode(root_val)
    root_index = inorder.index(root_val)
    root.left = binary_tree_from_preorder_inorder_0(preorder, inorder[:root_index])
    root.right = binary_tree_from_preorder_inorder_0(preorder, inorder[root_index+1:])
    return root

def binary_tree_from_preorder_inorder_1(preorder: List[int], inorder: List[int]) -> BinaryTreeNode:
    inorder_value_to_index = {v: k for k, v in enumerate(inorder)}
    def helper(preorder: List[int], inorder: List[int]) -> BinaryTreeNode:
        if not inorder:
            return
        root_val = preorder.pop(0)
        root = BinaryTreeNode(root_val)
        root_index = inorder_value_to_index[root_val]
        root.left = binary_tree_from_preorder_inorder_1(preorder, inorder[:root_index])
        root.right = binary_tree_from_preorder_inorder_1(preorder, inorder[root_index+1:])
        return root
    return helper(preorder, inorder)

def binary_tree_from_preorder_inorder(preorder: List[int], inorder: List[int]) -> BinaryTreeNode:
    inorder_value_to_index = {v: k for k, v in enumerate(inorder)}
    def helper(preorder_start: int, preorder_end: int, inorder_start: int, inorder_end) -> BinaryTreeNode:
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return
        root_val = preorder[preorder_start]
        root_index = inorder_value_to_index[root_val]
        left_subtree_size = root_index - inorder_start
        return BinaryTreeNode(
            root_val,
            helper(preorder_start + 1, preorder_start + 1 + left_subtree_size, inorder_start, root_index),
            helper(preorder_start + 1 + left_subtree_size, preorder_end, root_index + 1, inorder_end)
        )
    return helper(0, len(preorder), 0, len(inorder))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
