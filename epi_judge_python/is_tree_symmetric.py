from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:

    def are_two_trees_mirrored(tree_0: BinaryTreeNode, tree_1: BinaryTreeNode) -> bool:
        if tree_0 and tree_1:
            return tree_0.data == tree_1.data and are_two_trees_mirrored(tree_0.left, tree_1.right) and are_two_trees_mirrored(tree_0.right, tree_1.left)
        elif not tree_0 and not tree_1:
            return True
        else:
            return False

    return not tree or are_two_trees_mirrored(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
