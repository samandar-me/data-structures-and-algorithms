class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if mid > 0 and nums[mid] < nums[mid-1]:
                right = mid - 1
            elif mid < n - 1 and nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                return mid
        return 0
