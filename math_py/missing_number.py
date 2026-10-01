class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = n * (n + 1) // 2
        return total_sum - sum(nums)

    # def missingNumber(self, nums: list[int]) -> int:
    #     if not nums: return 0
    #
    #     expected = list(range(0, (max(nums) + 2)))
    #     set_nums = set(nums)
    #
    #     for n in expected:
    #         if not n in set_nums:
    #             return n

        # nums.sort()
        # n = len(nums)
        # i = 0
        #
        # while i < n - 1:
        #     if nums[i + 1] - nums[i] > 1:
        #         return i + 1
        #     i += 1
        #
        # return i + 1