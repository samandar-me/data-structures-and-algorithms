from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        original = k

        while True:
            if k not in nums:
                return k
            k += original