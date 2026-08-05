from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])

        answer = window_sum

        for right in range(k, len(nums)):
            window_sum += nums[right]
            window_sum -= nums[right-k]
            answer = max(answer, window_sum)

        return answer / k