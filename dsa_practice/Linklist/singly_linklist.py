class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class SinglyLinkList:
    def __init__(self):
        self.head = self.tail = None
        self.count = 0
       

    def insert(self,value):
        node = Node(value)
        if self.head == None and self.tail == None:
            self.head = self.tail = node
        else:
            self.tail.next = node
        self.count +=1
        self.tail = node
        

    def print_node(self):
        node = self.head
        while node:
            print({'value':node.value, 'next': node.next.value if node.next else node.next})
            node = node.next

    def delete_node(self, value):
        node = self.head
        if node.value == value:
            self.head = self.head.next
            if self.head.next is None:
                self.tail = None
            self.count -=1
            return True
        while node:
            if node.next and node.next.value == value:
                if node.next.next is None:
                    self.tail = node
                node.next = node.next.next
                self.count -=1
                return True
            else:
                node = node.next
        return False
    
    def reverse_link_list(self):
        current = self.head
        previous = None
        succeeding = None
        
        while current:
            succeeding = current.next
            current.next = previous
            previous = current
            current = succeeding
        self.head = previous

        
link_list = SinglyLinkList()
link_list.insert(5)
link_list.insert(6)
link_list.insert(7)
link_list.insert(8)
link_list.print_node()
link_list.reverse_link_list()
print("*********************")
link_list.print_node()