import functools
from typing import Optional

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from typing import List

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size


def find_kth_node_binary_tree_0(tree: BinaryTreeNode,
                              k: int) -> Optional[BinaryTreeNode]:
    l = []
    def helper(tree: BinaryTreeNode, l: List[BinaryTreeNode]):
        if tree:
            helper(tree.left, l)
            l.append(tree)
            helper(tree.right, l)

    helper(tree, l)
    return l[k - 1]

def find_kth_node_binary_tree(tree: BinaryTreeNode, k: int) -> Optional[BinaryTreeNode]:
    while tree:
        left_tree_size = tree.left.size if tree.left else 0
        if k > left_tree_size + 1:
            # kth is on the right
            k -= left_tree_size + 1
            tree = tree.right
        elif k == left_tree_size + 1:
            return tree
        else:
            tree = tree.left
    return None

@enable_executor_hook
def find_kth_node_binary_tree_wrapper(executor, tree, k):
    def init_size(node):
        if not node:
            return 0
        node.size = 1 + init_size(node.left) + init_size(node.right)
        return node.size

    init_size(tree)

    result = executor.run(functools.partial(find_kth_node_binary_tree, tree,
                                            k))

    if not result:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_node_in_tree.py',
                                       'kth_node_in_tree.tsv',
                                       find_kth_node_binary_tree_wrapper))
