class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res, sol = [], []

        def backtrack(total_sum=0):
            if len(sol) == k:
                if total_sum == n:
                    res.append(sol.copy())
                return

            for ni in range(sol[-1] + 1 if sol else 1, 10):
                if total_sum + ni > n:
                    break
                sol.append(ni)
                backtrack(total_sum + ni)
                sol.pop()

        backtrack()

        return res


    ##[[1, 2, 6], [1, 3, 5], [1, 5, 3], [2, 3, 4], [2, 4, 3], [3, 2, 4], [4, 2, 3]]