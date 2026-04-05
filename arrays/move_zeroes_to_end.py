#Question

# Pushing Zeros Back
#
# Move the zeros in the given list of numbers to the register, but do not disturb the sequence of other elements.
#
# Do as much as possible.
#
# Do not use additional memory - perform the operations on the list.
#
# Example 1:
#
# Input: numbers = [0,1,0,3,12]
# Result: [1, 3, 12, 0, 0]
# Example 1:
#
# Input: numbers = [0]
# Result: [0]


#Solution:

def moveZeroes(nums: list) -> list:
    for num in nums:
        if num == 0:
            index_of_zero = nums.index(num)
            nums += [nums.pop(index_of_zero)]

    return nums