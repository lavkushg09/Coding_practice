class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.adjacent_list = []
        self.visited = False


class Graph:
    def BFS(self, node):
        queue = []
        queue.append(node)
        node.visited = True

        traversal = []

        while queue:
            node = queue.pop(0)
            for n in node.adjacent_list:
                if not n.visited :
                    queue.append(n)
                    n.visited = True
            traversal.append(node.value)
        return traversal





node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
# node1 = Node("A")


node1.adjacent_list.append(node2)
node1.adjacent_list.append(node3)
node1.adjacent_list.append(node4)
node2.adjacent_list.append(node5)
node2.adjacent_list.append(node6)
node4.adjacent_list.append(node7)

node3.adjacent_list.append(node1)

graph = Graph()
print(graph.BFS(node1))