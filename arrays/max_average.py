class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k])
        answer = window_sum

        for right in range(k, len(nums)):
            window_sum -= nums[right-k]
            window_sum += nums[right]
            answer = max(answer, window_sum)

        return answer / k