class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            # find pivot index
            if 0 < mid < n - 1 and nums[mid - 1] > nums[mid] and nums[mid + 1] > nums[mid]:
                if nums[mid] < target:
                    pass


        return -1
