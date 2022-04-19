from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def postorder_traversal(tree: BinaryTreeNode) -> List[int]:
    in_process = [(tree, False)]
    result = []
    while in_process:
        node, is_every_subtree_traversed = in_process.pop()
        if not node:
            continue
        if is_every_subtree_traversed:
            result.append(node.data)
        else:
            in_process.append((node, True))
            in_process.append((node.right, False))
            in_process.append((node.left, False))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_postorder.py',
                                       'tree_postorder.tsv',
                                       postorder_traversal))
