from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        for i in range(len(nums)-2):
            if i < i + 1 < i + 2 and nums[i] < nums[i + 1] < nums[i + 2]:
                return True

        return False