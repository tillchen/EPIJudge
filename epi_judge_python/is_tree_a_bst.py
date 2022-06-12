from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import namedtuple
from collections import deque


def is_binary_tree_bst_0(tree: BinaryTreeNode, lower_bound = float('-inf'), upper_bound = float('inf')) -> bool:
    if not tree:
        return True
    if not lower_bound <= tree.data <= upper_bound:
        return False
    return is_binary_tree_bst_0(tree.left, lower_bound, tree.data) and is_binary_tree_bst_0(tree.right, tree.data, upper_bound)

def is_binary_tree_bst_1(tree: BinaryTreeNode) -> bool:
    inorder_path = []
    def inorder_traversal(tree: BinaryTreeNode):
        if not tree:
            return
        inorder_traversal(tree.left)
        inorder_path.append(tree)
        inorder_traversal(tree.right)

    inorder_traversal(tree)
    for i in range(1, len(inorder_path)):
        if inorder_path[i].data < inorder_path[i - 1].data:
            return False
    return True

def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    NodeWithBounds = namedtuple('NodeWithBounds', 'node lower upper')
    queue = deque()
    queue.append(NodeWithBounds(tree, float('-inf'), float('inf')))
    while queue:
        current = queue.popleft()
        if current.node:
            if not current.lower <= current.node.data <= current.upper:
                return False
            queue.append(NodeWithBounds(current.node.left, current.lower, current.node.data))
            queue.append(NodeWithBounds(current.node.right, current.node.data, current.upper))
    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
