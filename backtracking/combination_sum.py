class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res, sol = [], []
        n = len(candidates)

        def backtrack(total_sum=0):
            if total_sum == target:
                res.append(sol[:])
                return

            for i in range(sol[-1] if sol else 0, n):
                sol.append(candidates[i])
                backtrack(total_sum + candidates[i])
                sol.pop()

        backtrack()

        return res