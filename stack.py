class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
        
    def size(self):
        return len(self.items)
    
myStack = Stack()

myStack.push(1)
print(myStack.peek())
myStack.push(10)
print(myStack.peek())
print(myStack.size())
print(myStack.pop())
print(myStack.size())
print(myStack.peek())