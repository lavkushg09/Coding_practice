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