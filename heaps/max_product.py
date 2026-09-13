import heapq
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)

        first, second = heapq.heappop(nums), heapq.heappop(nums)

        return (abs(first) - 1) * (abs(second) - 1) 