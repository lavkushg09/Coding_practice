from PrettyPrint import PrettyPrintTree
from PrettyPrint import PrettyPrintLinkedList
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None



class ConstructBinaryTree:
    def build_binary_tree(self, pre_order, in_order):
        """
        Time complexity is O(n)
        Args:
            pre_order : list of node
            in_order : list of node

        Returns:
            node: node instance
        """
        memory = {value: inx for inx , value in enumerate(in_order)}
        return self.build_helper(pre_order[::-1], in_order, 0, len(in_order), memory)


    def build_helper(self, pre_order, in_order, left_pointer, right_pointer, memory):
        if left_pointer>=right_pointer:
            return None
        root = pre_order.pop()
        index = memory.get(root)
        node = Node(root)
        node.left = self.build_helper(pre_order, in_order, left_pointer, index, memory)
        node.right = self.build_helper(pre_order, in_order, index+1, right_pointer, memory)
        return node

    def construct_binary_tree(self, pre_order:list, in_order:list):
        # Time complexity is O(n2)
        root_value = pre_order.pop(0)
        if len(in_order) == 1:
            return Node(in_order[0])
        elif len(in_order) <1:
            return None
        
        node_ins = Node(root_value)
        index = self.find_index_of_element(root_value, in_order)
        left_side = self.construct_binary_tree(pre_order, in_order[:index])
        right_side = self.construct_binary_tree(pre_order, in_order[index+1:])
        node_ins.left = left_side
        node_ins.right = right_side
        return node_ins


    def find_index_of_element(self, value, list_inst):
        for inx in range(len(list_inst)):
            if list_inst[inx] == value:
                return inx
        return -1
    
    def invert_binary_tree(self, root_node):
        if root_node is None:
            return root_node
        left = self.invert_binary_tree(root_node.right)
        right = self.invert_binary_tree(root_node.left)
        root_node.left = left
        root_node.right = right
        return root_node
    
cb = ConstructBinaryTree()
pre_order = [1,2,4,8,9,5,10,11,3,6,7]
in_order = [8,4,9,2,10,5,11,1,6,3,7]
res = cb.build_binary_tree(pre_order, in_order)
# res = cb.construct_binary_tree(pre_order, in_order)

pt = PrettyPrintTree(
    lambda x: [x for x in [x.left, x.right] if x is not None],
    lambda x: x.value
)
pt(res)
in_res = cb.invert_binary_tree(res)
pt(in_res)