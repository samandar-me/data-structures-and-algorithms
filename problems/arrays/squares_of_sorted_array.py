# List Square
#
# You are given a list of numbers sorted in ascending order. Calculate the square of each element and return the result sorted.
#
# Example 1:
#
# Input: nums = [-4,-1,0,3,10]
# Result: [0,1,9,16,100]
# Example 2:
#
# Input: nums = [-7,-3,2,3,11]
# Result: [4,9,9,49,121]


def sortedSquares(nums: list) -> list:
    n = len(nums)
    result = [0] * n

    left = 0
    right = n - 1

    for write_index in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[write_index] = nums[left] ** 2
            left = left + 1
        else:
            result[write_index] = nums[right] ** 2
            right = right - 1

    return result
