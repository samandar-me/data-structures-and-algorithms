class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res, sol = [], []
        n = len(candidates)
        candidates.sort()

        def backtrack(start=0, total_sum=0):
            if total_sum == target:
                res.append(sol[:])
                return

            for i in range(start, n):
                if total_sum + candidates[i] > target:
                    break
                sol.append(candidates[i])
                backtrack(i, total_sum + candidates[i])
                sol.pop()

        backtrack()

        return res