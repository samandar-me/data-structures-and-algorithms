from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_to_index = {}

        for i in range(len(nums)):
            if nums[i] in num_to_index:
                if abs(num_to_index[nums[i]] - i) <= k:
                    return True
            num_to_index[nums[i]] = i

        return False

    # def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    #     seen = set()
    #
    #     left = 0
    #
    #     for right in range(len(nums)):
    #         if right - left > k:
    #             seen.remove(nums[left])
    #             left += 1
    #
    #         if nums[right] in seen:
    #             return True
    #         seen.add(nums[right])
    #
    #     return False