from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum1 = sum(nums)
        sum2 = 0

        for i in range(n+1):
            sum2 += i

        return sum2 - sum1

    # Solution 1
    # def missingNumber(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     nums.sort()
    #
    #     if nums[0] != 0:
    #         return 0
    #
    #     for i in range(len(nums) - 1):
    #         sum = nums[i + 1] - nums[i]
    #
    #         if sum > 1:
    #             return nums[i] + 1
    #
    #     return nums[n - 1] + 1

    # from typing import List
    #
    # from sliding_window.product_except_self import Solution
    #
    # def missingNumber(nums: List[int]) -> int:
    #     n = len(nums)
    #     s = (1 + n) * n // 2
    #     for num in nums:
    #         s -= num
    #
    #     return s
