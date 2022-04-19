from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    previous = None
    result = []
    while tree:
        if previous is tree.parent:
            # Came down from parent.
            if tree.left:
                next_ = tree.left
            else:
                result.append(tree.data)
                next_ = tree.right or tree.parent
        elif previous is tree.left:
            # Came up from the left.
            result.append(tree.data)
            next_ = tree.right or tree.parent
        else:
            # Came up from the right. Done.
            next_ = tree.parent
        previous = tree
        tree = next_
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
