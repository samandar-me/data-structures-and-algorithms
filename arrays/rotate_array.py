class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        temp_list = []

        for i in range(n-k, n):
            temp_list.append(nums[i])

        for i in range(n-k):
            temp_list.append(nums[i])

        for j in range(n):
            nums[j] = temp_list[j]