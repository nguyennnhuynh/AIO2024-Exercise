class MyStack:
    def __init__(self, capacity):
        self._capacity = capacity
        self._stack = []

    def is_empty(self):
        return len(self._stack) == 0

    def is_full(self):
        return len(self._stack) == self._capacity

    def pop(self):
        if self.is_empty():
            raise Exception("Underflow")
        return self._stack.pop()

    def push(self, value):
        if self.is_full():
            raise Exception("Overflow")
        self._stack.append(value)

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._stack[-1]

# Kiểm tra class MyStack
stack1 = MyStack(capacity=5)

stack1.push(1)
stack1.push(2)

print(stack1.is_full())  # False
print(stack1.top())  # 2
print(stack1.pop())  # 2
print(stack1.top())  # 1
print(stack1.pop())  # 1
print(stack1.is_empty())  # True