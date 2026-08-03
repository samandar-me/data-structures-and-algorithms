from collections import Counter
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        nums.sort()
        i = 0
        j = len(nums) - 1

        while i < j:
            s = nums[i] + nums[j]
            if s == k:
                operations += 1
                i += 1
                j -= 1
            elif s > k:
                j -= 1
            else:
                i += 1

        return operations

    # def maxOperations(self, nums: List[int], k: int) -> int:
    #     operations = 0
    #
    #     seen = set()
    #
    #     for num in nums:
    #         pair = k - num
    #         if pair in seen:
    #             operations += 1
    #             seen.remove(pair)
    #         else:
    #             seen.add(num)
    #
    #     return operations

    # def maxOperations(self, nums: List[int], k: int) -> int:
    #     counter = Counter(nums)
    #     operations = 0
    #
    #     for num in nums:
    #         complement = k - num
    #         count_of_num = counter.get(num, 0)
    #         count_of_complement = counter.get(complement, 0)
    #         if num == complement and count_of_complement > 1:
    #             operations += 1
    #             counter[complement] = counter.get(complement, 0) - 2
    #         elif num == complement and count_of_complement == 1:
    #             continue
    #         elif count_of_complement > 0 and count_of_num > 0:
    #             operations += 1
    #             counter[num] = counter.get(num, 0) - 1
    #             counter[complement] = counter.get(complement, 0) - 1
    #
    #     return operations