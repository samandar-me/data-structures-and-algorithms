class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        sett = set(nums)
        minn = min(nums)
        maxx = max(nums)
        i = minn
        longest = 0

        while i <= maxx:
            if i not in sett:
                i -= 1
                break
            i += 1
            longest += 1

        return longest