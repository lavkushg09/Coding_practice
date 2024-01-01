class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left=None
        self.right =  None


class BinaryInvertTree:

    def invert_binary_tree(self, root_node):
        if root_node is None:
            return root_node
        left = self.invert_binary_tree(root_node.right)
        right = self.invert_binary_tree(root_node.left)
        root_node.left = left
        root_node.right = right
        return root_node