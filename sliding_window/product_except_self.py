from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        left_products = [1] * n
        right_products = [1] * n

        for i in range(1, n):
            left_products[i] = nums[i-1] * left_products[i-1]

        for i in range(n-2, -1, -1):
            right_products[i] = nums[i+1] * right_products[i+1]

        for i in range(n):
            result[i] = left_products[i] * right_products[i]

        return result

    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     result = [1] * n
    #
    #     result[0] = 1
    #
    #     for i in range(1, n):
    #         result[i] = nums[i-1] * result[i-1]
    #
    #     r = 1
    #     for i in range(n - 1, -1, -1):
    #         result[i] = result[i] * r
    #         r = r * nums[i]
    #
    #     return result



