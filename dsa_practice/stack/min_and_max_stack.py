class Stack:
    def __init__(self) -> None:
        self.value_store = []
        self.min_stack = []
        self.max_stack = []

    def push(self, item:int):
        self.value_store.append(item)
        if self.min_stack:
            if item<self.min_stack[-1]:
                self.min_stack.append(item)
        else:
            self.min_stack.append(item)

        if self.max_stack:
            if item > self.min_stack[-1]:
                self.max_stack.append(item)
        else:
            self.max_stack.append(item)


    def pop(self):
        if self.min_stack[-1] == self.value_store[-1]:
            self.min_stack.pop()
        value = self.value_store.pop()
        return value

    def top(self):
        if self.value_store: 
            return self.value_store[-1]
        raise ValueError(f"Stack is empty.")
    
    def get_min(self):
        if self.value_store:
            return self.min_stack[-1]
        raise ValueError(f"Stack is empty.")
    

stack = Stack()
print(stack.top())
stack.push(5)
stack.push(6)
stack.push(8)
stack.push(9)

print(stack.pop())
print(stack.top())
print(stack.pop())
print(stack.top())