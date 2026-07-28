from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        result = [False] * n

        max_candy = -1

        for candy in candies:
            if max_candy < candy:
                max_candy = candy

        for i in range(n):
            result[i] = (candies[i] + extraCandies) >= max_candy

        return result