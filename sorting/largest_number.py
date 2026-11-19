from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = n

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        largest = sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(largest)))