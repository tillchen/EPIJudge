import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    if not tree:
        return []
    result = [tree]

    def get_left_boundary(node: BinaryTreeNode):
        if not node or not node.left and not node.right:
            return
        result.append(node)
        if node.left:
            get_left_boundary(node.left)
        else:
            get_left_boundary(node.right)

    def get_right_boundary(node: BinaryTreeNode):
        if not node or not node.left and not node.right:
            return
        if node.right:
            get_right_boundary(node.right)
        else:
            get_right_boundary(node.left)
        result.append(node)

    def get_leaves(node: BinaryTreeNode):
        if not node:
            return
        if not node.left and not node.right and node is not tree:
            result.append(node)
        get_leaves(node.left)
        get_leaves(node.right)

    get_left_boundary(tree.left)
    get_leaves(tree)
    get_right_boundary(tree.right)

    return result




def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',
                                       create_output_list_wrapper))
