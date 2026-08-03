from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_min = float("inf")
        second_min = float("inf")

        for num in nums:
            if num <= first_min:
                first_min = num
            elif num <= second_min:
                second_min = num
            else:
                return True

        return False

    # def increasingTriplet(self, nums: List[int]) -> bool:
    #     for i in range(len(nums)):
    #         counter = 0
    #         last_n = nums[i]
    #         for j in range(i+1, len(nums)):
    #             if nums[i] < nums[j] and last_n < nums[j]:
    #                 counter += 1
    #                 last_n = nums[j]
    #             if nums[i] < nums[j] < last_n:
    #                 last_n = nums[j]
    #
    #         if counter >= 2:
    #             return True
    #
    #     return False