class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res, sol = [], []
        n = len(candidates)
        candidates.sort()

        def backtrack(i=0, total_sum=0):
            if total_sum == target:
                res.append(sol[:])
                return

            while i < n:
                if total_sum + candidates[i] > target:
                    break
                sol.append(candidates[i])
                backtrack(i, total_sum + candidates[i])
                i += 1
                sol.pop()

        backtrack()

        return res