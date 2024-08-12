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
    
    def is_empty(self):
        if len(self.value_store):
            return False
        return True
    

# stack = Stack()
# print(stack.top())
# stack.push(5)
# stack.push(6)
# stack.push(8)
# stack.push(9)

# print(stack.pop())
# print(stack.top())
# print(stack.pop())
# print(stack.top())



# examples

# Find a string is balanced or not if `{[(){}]}`

# 1st version
def is_balanced(string_ins):
    stack = Stack()
    for char in string_ins:
        if char in ['[','{','(']:
            stack.push(char)
        elif char in ['}',']',')']:
            last_value = stack.pop()
            if last_value == '(':
                if char != ')':
                    return False
            elif last_value == '{':
                if char != '}':
                    return False
            elif last_value == '[':
                if char != ']':
                    return False
            else:
                return False
        else:
            return False
    if len(stack.value_store) == 0:
        return True
    
# 2nd version
def is_balanced_v2(string_ins):
    stack = Stack()
    brackets_map = {')':'(','}':'{',']':'['}
    for char in string_ins:
        if char in brackets_map.values():
            stack.push(char)
        elif char in brackets_map:
            if stack.is_empty() or stack.pop() != brackets_map[char]:
                return False
        else:
            return False
        
    if stack.is_empty():
        return True

print(is_balanced_v2("{[()]}"))


