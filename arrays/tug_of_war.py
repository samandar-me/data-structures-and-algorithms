# Tug of war
#
# Each child is given a list of their strengths. For each child, determine which side would win if they were the referee and the players ahead and behind them on the list were playing tug of war.
#
# The team with the highest combined strength wins.
#
# Condition Result
# If the players ahead of the referee win -1
# If the players behind the referee win 1
# If the players are tied 0
# Example 1:
#
# Input: [1, 2, 3, 4]
# Output: [1, 1, 1, -1]
# Example 2:
#
# Input: [10, 4, 8, 3]
# Output: [1, 1, -1, -1]

def leftRightDifference(nums: list) -> list:
    result = []
    total_sum = sum(nums)
    left_sum = 0

    for i in range(len(nums)):
        current_referee = nums[i]
        right_sum = total_sum - left_sum - current_referee

        if left_sum > right_sum:
            result.append(-1)
        elif right_sum > left_sum:
            result.append(1)
        else:
            result.append(0)

        left_sum = left_sum + current_referee

    return result