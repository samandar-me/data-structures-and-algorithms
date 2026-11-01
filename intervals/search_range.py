class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]

        target_index = self.binary_search(target, nums)
        if target == -1:
            return [-1, -1]

        start = -1
        end = -1
        left = 0
        right = target_index

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                start = mid
                right = mid - 1
            else:
                left = mid + 1

        left = target_index
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                end = mid
                left = mid + 1
            else:
                right = mid - 1


        return [start, end]

    def binary_search(self, target, nums) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1