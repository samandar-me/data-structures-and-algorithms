from ast import List


from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        original_array = nums.copy()
        nums.sort()

        left = 0
        right = len(nums) - 1

        while left <= right:
            sum = nums[left] + nums[right]

            if sum == target:
                org_index1 = self.findOriginalIndexLeft(original_array, nums[left])
                org_index2 = self.findOriginalIndexRight(original_array, nums[right])
                return [org_index1, org_index2]

            if sum > target:
                right = right - 1
            else:
                left = left + 1

        return []


    def findOriginalIndexLeft(self, nums: List[int], target: int):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return None

    def findOriginalIndexRight(self, nums: List[int], target: int):
        for i in reversed(range(len(nums))):
            if nums[i] == target:
                return i
        return None

    # Solution 1, did not work for some cases
    #
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     result = []
    #     nums.sort()
    #
    #     for i in range(len(nums) - 1):
    #         sum = nums[i] + nums[i + 1]
    #
    #         if sum == target:
    #             result.append(i)
    #             result.append(i + 1)
    #
    #     return result