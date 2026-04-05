# The pool with the most water
#
# You are given the heights of the walls, spaced 1 meter apart. How much water can the two walls that can hold the most water hold?
#
# Example 1:
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: 7 * 7 = 49
#
# Input: [1,1]
# Output: 1

def maxArea(nums: list) -> int:
    left = 0
    right = len(nums) - 1
    max_water = 0

    while left < right:
        width = right - left
        current_height = min(nums[left], nums[right])
        current_area = width * current_height
        max_water = max(max_water, current_area)

        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1

    return max_water