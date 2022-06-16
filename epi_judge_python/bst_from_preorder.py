from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder_0(preorder_sequence: List[int]) -> Optional[BstNode]:
    if not preorder_sequence:
        return
    pivot = next((i for i, a in enumerate(preorder_sequence) if a > preorder_sequence[0]), len(preorder_sequence))
    return BstNode(preorder_sequence[0], rebuild_bst_from_preorder(preorder_sequence[1:pivot]), rebuild_bst_from_preorder(preorder_sequence[pivot:]))

def rebuild_bst_from_preorder(preorder_sequence: List[int]) -> Optional[BstNode]:
    if not preorder_sequence:
        return
    pivot = len(preorder_sequence)
    for i, a in enumerate(preorder_sequence):
        if a > preorder_sequence[0]:
            pivot = i
            break
    return BstNode(preorder_sequence[0], rebuild_bst_from_preorder(preorder_sequence[1:pivot]), rebuild_bst_from_preorder(preorder_sequence[pivot:]))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
