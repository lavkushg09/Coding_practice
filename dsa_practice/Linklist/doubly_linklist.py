class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class DoublyNode(Node):
    def __init__(self, value=None, next=None):
        super().__init__(value, next)
        self.previous = None


class DoublyLinkList:
    def __init__(self) -> None:
        self.head = self.tail = None
        self.size = 0

    def get(self, index:int) -> int:
        if index<0 and self.size < index:
            return -1
        node = self.head
        while index !=0:
            node = node.next
            index -=1
        return node.value
    
    def add_at_head(self, value):
        node = DoublyNode(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.head.previous = node
            node.next = self.head
            self.head = node
        self.size +=1

    def add_at_tail(self, value):
        node = DoublyNode(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        self.size +=1

    def add_at_index(self, index:int, value)->bool:
        if index<0 and index>self.size:
            return False
        new_node = DoublyNode(value)
        node = self.head
        while index !=0:
            node = node.next
            index -=1
        new_node.previous = node.previous
        new_node.next = node
        node.previous.next = new_node
        node.previous = new_node
        self.size +=1
        return True
    
    
    def delete_at_index(self, index:int):
        if index<0 and index>self.size:
            return False
        
        node = self.head
        while index !=0:
            node = node.next
            index -=1

        if node.next is None and node.previous is None:
            self.head = self.tail = None
            self.size = 0
            return True
        
        if node.next:
            node.next.previous = node.previous
        else:
            node.previous.next = None
            self.tail = node.previous

        if node.previous:
            node.previous.next = node.next
        else:
            node.next.previous = None
            self.head = node.next
        
        self.size -=1
        return True
    
    def reverse_link_list(self):
        import time
        node = self.head
        while node:
            next_node =  node.next
            previous_node = node.previous
            node.next = previous_node
            node.previous = next_node
            if next_node is None:
                self.head = node

            if previous_node is None:
                self.tail = node
            node = next_node 
            

        


         


    def insert(self, value):
        self.add_at_tail(value)

    def print_node(self):
        node = self.head
        st = ""
        # print(self.head)
        print(self.size)
        while node:
            print({"previous":node.previous.value if node.previous else node.previous, 'value':node.value, 'next': node.next.value if node.next else node.next})
            node = node.next


doubly_link_list = DoublyLinkList()
doubly_link_list.insert(5)
doubly_link_list.add_at_tail(9)
doubly_link_list.insert(15)
doubly_link_list.insert(35)
doubly_link_list.add_at_head(11)
doubly_link_list.add_at_index(3,91)
# doubly_link_list.print_node()
doubly_link_list.delete_at_index(3)
# doubly_link_list.print_node()
doubly_link_list.delete_at_index(1)
doubly_link_list.print_node()
doubly_link_list.reverse_link_list()
doubly_link_list.print_node()