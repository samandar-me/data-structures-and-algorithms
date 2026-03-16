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


if __name__ == '__main__':
    print(maxArea([1,8,6,2,5,4,8,3,7]))