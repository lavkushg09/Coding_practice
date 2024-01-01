import time

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.adjacent_list = []
        self.visited = False


class Graph:
    def DFS(self, node, traversal=[]):
        traversal.append(node.value)
        node.visited = True
        for node_i in node.adjacent_list:
            if not node_i.visited:
                self.DFS(node_i, traversal)
        
        return traversal






node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")
node9 = Node("I")


node1.adjacent_list.append(node2)
node1.adjacent_list.append(node3)
node1.adjacent_list.append(node4)
node2.adjacent_list.append(node5)
node2.adjacent_list.append(node6)
node4.adjacent_list.append(node7)

node3.adjacent_list.append(node1)
node3.adjacent_list.append(node6)
node3.adjacent_list.append(node7)
node7.adjacent_list.append(node8)
node8.adjacent_list.append(node9)
node9.adjacent_list.append(node7)

graph = Graph()
print(graph.DFS(node1))