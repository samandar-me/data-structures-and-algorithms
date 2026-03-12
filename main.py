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

if __name__ == '__main__':
    print(sortedSquares([-4,-1,0,3,10]))