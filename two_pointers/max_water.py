from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            distance = right - left
            min_n = min(height[left], height[right])
            max_area = max(max_area, distance * min_n)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return int(max_area)