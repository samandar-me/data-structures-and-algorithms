from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        result = []
        expected_list = list(range(min(nums), max(nums)))
        seen = set(nums)

        for num in expected_list:
            if num not in seen:
                result.append(num)

        return result