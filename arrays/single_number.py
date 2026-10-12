from collections import Counter
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0

        for num in nums:
            xor ^= num

        return xor

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