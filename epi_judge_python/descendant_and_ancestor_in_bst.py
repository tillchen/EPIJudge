import functools

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook

def search_for_node(root: BstNode, target: BstNode) -> bool:
    current = root
    while current:
        if target.data < current.data:
            current = current.left
        elif target.data > current.data:
            current = current.right
        else:
            if current is root:
                return False
            return True
    return False


def pair_includes_ancestor_and_descendant_of_m_0(possible_anc_or_desc_0: BstNode, possible_anc_or_desc_1: BstNode, middle: BstNode) -> bool:
    return search_for_node(possible_anc_or_desc_0, middle) and search_for_node(middle, possible_anc_or_desc_1) or search_for_node(possible_anc_or_desc_1, middle) and search_for_node(middle, possible_anc_or_desc_0)

def pair_includes_ancestor_and_descendant_of_m(possible_anc_or_desc_0: BstNode, possible_anc_or_desc_1: BstNode, middle: BstNode) -> bool:
    search_0, search_1 = possible_anc_or_desc_0, possible_anc_or_desc_1
    # Interleaved search
    while (
        search_0 is not possible_anc_or_desc_1 and search_0 is not middle
        and search_1 is not possible_anc_or_desc_0 and search_1 is not middle
        and (search_0 or search_1)
    ):
        if search_0:
            search_0 = (search_0.left if search_0.data > middle.data else search_0.right)
        if search_1:
            search_1 = (search_1.left if search_1.data > middle.data else search_1.right)
    if (
        search_0 is not middle and search_1 is not middle
        or search_0 is possible_anc_or_desc_1
        or search_1 is possible_anc_or_desc_0
    ):
        return False

    def search_target(root: BstNode, target: BstNode) -> bool:
        while root and root is not target:
            root = root.left if root.data > target.data else root.right
        return root is target

    return search_target(middle, possible_anc_or_desc_0 if middle is search_1 else possible_anc_or_desc_1)

@enable_executor_hook
def pair_includes_ancestor_and_descendant_of_m_wrapper(executor, tree,
                                                       possible_anc_or_desc_0,
                                                       possible_anc_or_desc_1,
                                                       middle_idx):
    candidate0 = must_find_node(tree, possible_anc_or_desc_0)
    candidate1 = must_find_node(tree, possible_anc_or_desc_1)
    middle_node = must_find_node(tree, middle_idx)

    return executor.run(
        functools.partial(pair_includes_ancestor_and_descendant_of_m,
                          candidate0, candidate1, middle_node))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'descendant_and_ancestor_in_bst.py',
            'descendant_and_ancestor_in_bst.tsv',
            pair_includes_ancestor_and_descendant_of_m_wrapper))
