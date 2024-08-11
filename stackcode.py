class Stack:
    def __init__(self, n):
        self.stack = [None] * n
        self.top_index = -1
        self.n = n

    def size(self):
        return self.top_index + 1

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.n

    def push(self, value):
        if self.is_full():
            print("Stack is full")
            return
        self.top_index += 1
        self.stack[self.top_index] = value

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        value = self.stack[self.top_index]
        self.stack[self.top_index] = None  # Optional: Clear the popped spot
        self.top_index -= 1
        return value

    def top(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[self.top_index]

