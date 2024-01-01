from PrettyPrint import PrettyPrintTree
from PrettyPrint import PrettyPrintLinkedList

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self, value) -> None:
        self.root = Node(value)

    def pre_order(self, start, traversal=[]):
        """
        root -> left -> right
        """
        if start is None:
            return
        
        traversal.append(start.value)
        self.pre_order(start.left, traversal)
        self.pre_order(start.right, traversal)
        return traversal
    
    def in_order(self, start, traversal=[]):
        """
        left -> root -> right
        """
        if start is None:
            return
        
        
        self.in_order(start.left, traversal)
        traversal.append(start.value)
        self.in_order(start.right, traversal)
        return traversal
    
    def post_order(self, start, traversal=[]):
        """
        left -> right -> root
        """
        if start is None:
            return
        
        
        self.post_order(start.left, traversal)
        self.post_order(start.right, traversal)
        traversal.append(start.value)
        return traversal



tree = BinaryTree(3)
tree.root.left = Node(4)
tree.root.left.left = Node(6)
tree.root.left.right = Node(7)


tree.root.right = Node(5)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)
pt = PrettyPrintTree(
    lambda x: [x for x in [x.left, x.right] if x is not None],
    lambda x: x.value
)
pt(tree.root)

print(f"pre order traversal ==> {tree.pre_order(tree.root)}")
print(f"in order traversal ==> {tree.in_order(tree.root)}")
print(f"post order traversal ==> {tree.post_order(tree.root)}")
