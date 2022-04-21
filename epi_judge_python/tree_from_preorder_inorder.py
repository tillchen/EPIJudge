from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    if not inorder:
        return
    root_val = preorder.pop(0)
    root = BinaryTreeNode(root_val)
    root_index = inorder.index(root_val)
    root.left = binary_tree_from_preorder_inorder(preorder, inorder[:root_index])
    root.right = binary_tree_from_preorder_inorder(preorder, inorder[root_index+1:])
    return root



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
