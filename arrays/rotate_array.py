class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        original = nums.copy()
        if k > len(nums):
            nums += nums
        last_k_nums = nums[-k:] if k > 0 else []

        print(nums)
        i = 0
        for n in last_k_nums:
            nums[i] = n
            i += 1

        for j in range(len(nums)-k):
            nums[i] = original[j]
            i += 1

        for _ in range(len(original)):
            nums.pop()

        print(nums)