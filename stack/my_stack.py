class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1

        return self.stack.pop()

    def top(self) -> int:
        if self.empty():
            return -1

        last_element = self.stack[len(self.stack) - 1]
        return last_element

    def empty(self) -> bool:
        return len(self.stack) == 0

    def print(self) -> None:
        print(self.stack)