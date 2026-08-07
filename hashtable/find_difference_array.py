from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums_set1 = set(nums1)
        nums_set2 = set(nums2)

        answer = [[], []]

        seen1 = set()
        seen2 = set()

        for num in nums2:
            if num not in nums_set1 and num not in seen1:
                answer[1].append(num)
                seen1.add(num)

        for num in nums1:
            if num not in nums_set2 and num not in seen2:
                answer[0].append(num)
                seen2.add(num)

        return answer