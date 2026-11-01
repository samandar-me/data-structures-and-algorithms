from intervals.search_range import Solution

if __name__ == '__main__':
    solution = Solution()

    print(solution.searchRange(nums = [5,7,7,8,8,10], target = 8))
    print(solution.searchRange(nums = [5,7,7,8,8,10], target = 6))
    print(solution.searchRange(nums = [], target = 0))
    print(solution.searchRange([1, 1, 2, 2, 2, 2, 2, 3, 4, 4, 5], target = 2))

