import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca_0(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    set_of_nodes = set()
    while node0:
        set_of_nodes.add(node0)
        node0 = node0.parent
    while node1:
        if node1 in set_of_nodes:
            return node1
        node1 = node1.parent
    return None

def lca(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    def get_depth(node: BinaryTreeNode) -> int:
        depth = 0
        while node:
            depth += 1
            node = node.parent
        return depth

    depth0, depth1 = get_depth(node0), get_depth(node1)
    # Let node0 be the deeper one.
    if depth1 > depth0:
        node0, node1 = node1, node0
        depth0, depth1 = depth1, depth0
    while depth1 < depth0:
        node0 = node0.parent
        depth0 -= 1
    while node0 is not node1:
        node0 = node0.parent
        node1 = node1.parent
    return node0


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
