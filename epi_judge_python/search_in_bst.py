from typing import Optional

from bst_node import BstNode
from test_framework import generic_test

def search_bst_0(tree: BstNode, key: int) -> Optional[BstNode]:
    if not tree or key == tree.data:
        return tree
    if key < tree.data:
        return search_bst_0(tree.left, key)
    return search_bst_0(tree.right, key)

def search_bst(tree: BstNode, key: int) -> Optional[BstNode]:
    while tree:
        if key < tree.data:
            tree = tree.left
        elif key > tree.data:
            tree = tree.right
        else:
            return tree
    return None


def search_bst_wrapper(tree, key):
    result = search_bst(tree, key)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_in_bst.py', 'search_in_bst.tsv',
                                       search_bst_wrapper))
