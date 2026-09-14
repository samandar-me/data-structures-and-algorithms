import heapq

class SmallestInfiniteSet:
    heap = []
    numbers = set()

    def __init__(self):
        self.heap = []
        self.numbers = set()

        for i in range(1, 1001):
            self.heap.append(i)
            self.numbers.add(i)

        heapq.heapify(self.heap)

    def popSmallest(self) -> int:
        num = heapq.heappop(self.heap)
        self.numbers.remove(num)
        return num

    def addBack(self, num: int) -> None:
        if num not in self.numbers:
            heapq.heappush(self.heap, num)
            self.numbers.add(num)