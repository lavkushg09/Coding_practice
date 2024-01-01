class Queue:
    def __init__(self) -> None:
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items)>0:
            return self.items.pop(0)
        
    def peek(self):
        if len(self.items)>0:
            return self.items[0].value

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None


# class BinaryTree:
#     def __init__(self, value) -> None:
#         self.root = Node(value)

#     def level_order(self, start):
#         traversal=[]
#         queue = [start]
#         i=0
#         while i<len(queue):
#             current_element = queue[i]
#             if current_element.left:
#                 queue.append(current_element.left)
#             if current_element.right:
#                 queue.append(current_element.right)
#             traversal.append(current_element.value)
#             i +=1
#         return traversal
        
class BinaryTree:
    def __init__(self, value) -> None:
        self.root = Node(value)

    def level_order(self, start):
        traversal=[]
        qu = Queue()
        qu.enqueue(start)
        while qu.peek():
            current_element = qu.dequeue()
            if current_element.left:
                qu.enqueue(current_element.left)
            if current_element.right:
                qu.enqueue(current_element.right)
            traversal.append(current_element.value)
        return traversal
    




tree = BinaryTree(3)
tree.root.left = Node(4)
tree.root.left.left = Node(6)
tree.root.left.right = Node(7)


tree.root.right = Node(5)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)

print(f"pre order traversal ==> {tree.level_order(tree.root)}")

