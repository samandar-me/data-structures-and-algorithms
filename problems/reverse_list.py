# Rotate List
#
# Rotate the given list k steps to the right.
#
# Shifting the list 1 step to the right means placing the rightmost element at the beginning of the leftmost element.
#
# Perform the operation on the given list - do not create a new list.
#
# Example 1:
#
# Input: numbers = [1,2,3,4,5,6,7], k = 3
# Result: [5,6,7,1,2,3,4]
# Explanation:
# Step 1: [7,1,2,3,4,5,6]
# Step 2: [6,7,1,2,3,4,5]
# Step 3: [5,6,7,1,2,3,4]
# Example 2:
#
# Input: numbers = [-1,-100,3,99], k = 2
# Result: [3,99,-1,-100]
# Explanation:
# Step 1: [99,-1,-100,3]
# Step 2: [3,99,-1,-100]

#Solution:

def rotate(nums: list, k: int) -> list:
    if not nums:
        return nums

    k = k % len(nums)
    nums.reverse()
    nums[0:k] = reversed(nums[0:k])
    nums[k:len(nums)] = reversed(nums[k:len(nums)])
    return nums