class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res, sol = [], []
        n = len(nums)

        def backtrack():
            if len(sol) == n:
                res.append(sol[:])
                return

            for j in range(n):
                if nums[j] not in sol:
                    sol.append(nums[j])
                    backtrack()
                    sol.pop()

        backtrack()
        return res