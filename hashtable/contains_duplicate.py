def containsDuplicate(nums: list) -> bool:
    return len(set(nums)) != len(nums)

# def containsDuplicate(nums: list) -> bool:
# 	numbers = set()
#
# 	for i in range(len(nums)):
# 		if nums[i] in numbers:
# 			return True
# 		else:
# 			numbers.add(nums[i])
#
# 	return False

# def containsDuplicate(nums: list) -> bool:
# 	l1 = []
#
# 	for i in range(len(nums)):
# 		if contains(l1, nums[i]):
# 			return True
# 		else:
# 			l1.append(nums[i])
#
# 	return False
#
# def contains(nums: list, target: int) -> bool:
# 	for j in range(len(nums)):
# 		if target == nums[j]:
# 			return True
#
# 	return False