from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        first_index = min(min_index, max_index)
        second_index = max(min_index, max_index)

        front = second_index + 1
        back = n - first_index
        mixed = (first_index + 1) + (n - second_index)

        return min(front, back, mixed)

    # def minimumDeletions(self, nums: List[int]) -> int:
    #     n = len(nums)
    #
    #     if n <= 2:
    #         return n
    #
    #     middle = n // 2
    #
    #     min_value = min(nums)
    #     max_value = max(nums)
    #     index_of_min = nums.index(min_value)
    #     index_of_max = nums.index(max_value)
    #
    #     first_index = min(index_of_min, index_of_max)
    #     second_index = max(index_of_min, index_of_max)
    #
    #     if second_index <= middle:
    #         return second_index + 1
    #
    #     if first_index >= middle:
    #         return n - first_index
    #
    #     left = first_index + 1
    #     right = n - second_index
    #
    #     both_from_back = n - first_index
    #     both_from_front = second_index + 1
    #     smaller_side = min(both_from_front, both_from_back)
    #
    #     return min((left + right), smaller_side)