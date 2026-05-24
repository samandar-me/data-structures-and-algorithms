def twoSum(nums: list, target: int) -> list:
	compliments = {}

	for i, num in enumerate(nums):
		if num in compliments:
			return [compliments[num], i]

		compliments[target-num] = i

	return []

# def twoSum(nums: list, target: int) -> list:
# 	for i in range(len(nums)):
# 		for j in range(i + 1, len(nums)):
# 			if nums[i] + nums[j] == target:
# 				return [i, j]
#
# 	return []