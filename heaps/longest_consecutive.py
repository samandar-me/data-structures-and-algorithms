class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        left = 0
        longest = 0
        previous = nums[0]
        n = len(nums)

        for right in range(n):
            diff = abs(nums[right] - previous)
            previous = nums[right]

            if diff >= 2:
                # if left == 0:
                #     left = 1
                longest = max(longest, right - left + 1)
                left = right

            if right == n-1:
                if left == 0:
                    left = 1
                longest = max(longest, right - left + 1)

        return longest

    # def longestConsecutive(self, nums: list[int]) -> int:
    #     if not nums:
    #         return 0
    #     nums.sort()
    #     left = 0
    #     right = 0
    #     longest = 0
    #     previous = nums[0]
    #     n = len(nums)
    #
    #     for i in range(n):
    #         diff = abs(nums[i] - previous)
    #         previous = nums[i]
    #
    #         if diff == 0:
    #             right -= 1
    #         elif diff >= 2:
    #             longest = max(longest, right - left + 1)
    #             left = i
    #
    #         right += 1
    #         if i == n-1:
    #             longest = max(longest, right - left + 1)
    #
    #     return longest

    # def longestConsecutive(self, nums: list[int]) -> int:
    #     if not nums:
    #         return 0
    #     nums.sort()
    #     left = 0
    #     right = 0
    #     longest = 0
    #     nums.append(nums[-1])
    #
    #     for i in range(len(nums)-1):
    #         diff = abs(nums[i + 1] - nums[i])
    #
    #         if diff == 0:
    #             right -= 1
    #         elif diff >= 2:
    #             longest = max(longest, right - left + 1)
    #             left = i
    #         right += 1
    #
    #     return max(longest, right - left + 1)