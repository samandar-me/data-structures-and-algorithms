from typing import List
import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        heap = []
        n = len(score)
        result = ["0"] * n
        for i in range(n):
            heapq.heappush(heap, (-score[i], i))

        i = 0
        while i < n:
            _, index = heapq.heappop(heap)
            if i <= 2:
                result[index] = medals[i]
            else:
                result[index] = f"{i + 1}"

            i += 1

        return result