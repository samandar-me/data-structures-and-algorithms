from typing import List
from collections import Counter

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]

            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return -1




    # def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
    #     counter1 = Counter(nums1)
    #     counter2 = Counter(nums2)
    #
    #     smaller = nums1 if len(nums1) <= len(nums2) else nums2
    #
    #     for n in smaller:
    #         if counter1[n] and counter2[n]:
    #             return n
    #
    #     return -1

