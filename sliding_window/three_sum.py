class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        answer = []
        n = len(nums)

        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue

            low, high = i + 1, n - 1

            while low < high:
                summ = nums[i] + nums[low] + nums[high]
                if summ == 0:
                    answer.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1

                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                elif summ < 0:
                    low += 1
                else:
                    high -= 1

        return answer