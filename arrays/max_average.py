class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_average = sum(nums[:k])

        for right in range(k, len(nums)):
            window = nums[right - k]
            max_average = max((max_average + nums[right]), window)

        return max_average / k