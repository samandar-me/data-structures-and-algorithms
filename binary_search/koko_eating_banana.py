from math import ceil

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            k = left + ((right - left) // 2)
            total_hour = 0

            for pile in piles:
                total_hour += ceil(pile / k)

            if total_hour <= h:
                right = k - 1
            else:
                left = k + 1

        return left