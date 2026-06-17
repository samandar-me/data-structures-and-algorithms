from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 0

        while i < len(nums) - 1:
            if nums[i] != nums[i+1]:
                return nums[i]

            i += 2

        return nums[0]

    # def singleNumber(self, nums: List[int]) -> int:
    #     hash_map = {}
    #
    #     for n in nums:
    #         hash_map[n] = 1 + hash_map.get(n, 0)
    #
    #
    #     for k, v in hash_map.items():
    #         if v == 1:
    #             return k
    #
    #     return nums[0]