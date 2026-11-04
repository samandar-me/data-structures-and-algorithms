class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest

    # def longestConsecutive(self, nums: list[int]) -> int:
    #     if not nums:
    #         return 0
    #
    #     temp = []
    #     sett = set(nums)
    #     longest = 0
    #     minn = min(nums)
    #     maxx = max(nums)
    #
    #     for i in range(minn, maxx+1):
    #         if i not in sett:
    #             longest = max(longest, len(temp))
    #             temp.clear()
    #         else:
    #             temp.append(i)
    #
    #     return max(longest, len(temp))