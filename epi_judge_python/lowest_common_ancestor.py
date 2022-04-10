import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from collections import namedtuple

def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    Status = namedtuple('Status', 'num_of_target_nodes ancestor')

    def helper(tree: BinaryTreeNode, node0: BinaryTreeNode, node1: BinaryTreeNode) -> Status:
        if not tree:
            return Status(0, None)
        left_result = helper(tree.left, node0, node1)
        if left_result.num_of_target_nodes == 2:
            return left_result
        right_result = helper(tree.right, node0, node1)
        if right_result.num_of_target_nodes == 2:
            return right_result
        num_of_target_nodes = left_result.num_of_target_nodes + right_result.num_of_target_nodes + int(tree is node0) + int(tree is node1)
        return Status(num_of_target_nodes, tree if num_of_target_nodes == 2 else None)
    return helper(tree, node0, node1).ancestor


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
