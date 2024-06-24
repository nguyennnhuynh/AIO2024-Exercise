class MyQueue:
    def __init__(self, capacity):
        self._capacity = capacity
        self._queue = []

    def is_empty(self):
        return len(self._queue) == 0

    def is_full(self):
        return len(self._queue) == self._capacity

    def dequeue(self):
        if self.is_empty():
            raise Exception("Underflow")
        return self._queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            raise Exception("Overflow")
        self._queue.append(value)

    def front(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._queue[0]


# Kiểm tra class MyQueue
if __name__ == "__main__":
    queue1 = MyQueue(capacity=5)

    queue1.enqueue(1)
    queue1.enqueue(2)

    print(queue1.is_full())  # False
    print(queue1.front())  # 1
    print(queue1.dequeue())  # 1
    print(queue1.front())  # 2
    print(queue1.dequeue())  # 2
    print(queue1.is_empty())  # True
    