import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from collections import deque


class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.next = None  # Populates this field.


# BFS
def construct_right_sibling(tree: BinaryTreeNode) -> None:
    if not tree:
        return
    queue = deque()
    queue.append(tree)
    while queue:
        level = []
        for _ in range(len(queue)):
            current = queue.popleft()
            level.append(current)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        for i in range(len(level) - 1):
            level[i].next = level[i + 1]


def traverse_next(node):
    while node:
        yield node
        node = node.next
    return


def traverse_left(node):
    while node:
        yield node
        node = node.left
    return


def clone_tree(original):
    if not original:
        return None
    cloned = BinaryTreeNode(original.data)
    cloned.left, cloned.right = clone_tree(original.left), clone_tree(
        original.right)
    return cloned


@enable_executor_hook
def construct_right_sibling_wrapper(executor, tree):
    cloned = clone_tree(tree)

    executor.run(functools.partial(construct_right_sibling, cloned))

    return [[n.data for n in traverse_next(level)]
            for level in traverse_left(cloned)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_right_sibling.py',
                                       'tree_right_sibling.tsv',
                                       construct_right_sibling_wrapper))
