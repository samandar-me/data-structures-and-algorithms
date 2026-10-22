from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_array_count = 0
        seen = {0 : 1}
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            sub_array_count += seen.get(prefix_sum - k, 0)
            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

        return sub_array_count


    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     sub_array_count = 0
    #
    #     for i in range(len(nums)):
    #         current_sum = 0
    #         for j in range(i, len(nums)):
    #             current_sum += nums[j]
    #             sub_array_count += current_sum == k
    #
    #     return sub_array_count