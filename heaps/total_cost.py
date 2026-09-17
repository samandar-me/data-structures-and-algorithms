from typing import List
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []
        n = len(costs)
        total_cost = 0
        left = 0
        right = n - 1

        if  n <= candidates * 2:
            for i in range(n):
                heapq.heappush(heap, (costs[i], i, ""))
        else:
            for _ in range(candidates):
                heapq.heappush(heap, (costs[left], left, "left"))
                heapq.heappush(heap, (costs[right], right, "right"))
                left += 1
                right -= 1

        for _ in range(k):
            cost, index, side = heapq.heappop(heap)
            total_cost += cost

            if side == "left":
                if left <= right:
                    heapq.heappush(heap, (costs[left], left, "left"))
                    left += 1
            elif side == "right":
                if left <= right:
                    heapq.heappush(heap, (costs[right], right, "right"))
                    right -= 1

        return total_cost
