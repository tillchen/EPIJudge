from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    def helper(tree: BinaryTreeNode, path_sum: int) -> int:
        if not tree:
            return 0
        path_sum = path_sum * 2 + tree.data
        if not tree.left and not tree.right:
            return path_sum
        return helper(tree.left, path_sum) + helper(tree.right, path_sum)

    return helper(tree, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
