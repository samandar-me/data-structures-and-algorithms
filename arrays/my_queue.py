from collections import deque

class MyQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.popleft()

    def peek(self) -> int:
        if self.empty():
            return -1
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0

    def print(self) -> None:
        print(self.queue)