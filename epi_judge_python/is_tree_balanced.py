from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import namedtuple


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    BalancedStatusWithHeight = namedtuple('BalancedStatusWithHeight', 'is_balanced height')

    def check_balanced(tree: BinaryTreeNode) -> BalancedStatusWithHeight:
        if not tree:
            return BalancedStatusWithHeight(True, -1)
        left_result = check_balanced(tree.left)
        if not left_result.is_balanced:
            return BalancedStatusWithHeight(False, 0)
        right_result = check_balanced(tree.right)
        if not right_result.is_balanced:
            return BalancedStatusWithHeight(False, 0)
        is_balanced = abs(left_result.height - right_result.height) < 2
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).is_balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
