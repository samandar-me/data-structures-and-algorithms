from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1

        for i in range(index, len(nums)):
            nums[i] = 0

        print(nums)

    # def moveZeroes(self, nums: List[int]) -> None:
    #
    #     for n in nums:
    #         if n == 0:
    #             nums.append(0)
    #             nums.remove(0)


