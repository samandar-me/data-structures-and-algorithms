class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        n = len(spells)
        pn = len(potions)
        pairs = [0] * n

        for i in range(n):
            count = self.binary_search_count(spells[i], pn, potions, success)
            pairs[i] = count

        return pairs

    def binary_search_count(self, multiplier, pn, potions, success) -> int:
       left = 0
       right = pn - 1

       while left <= right:
           mid = left + ((right - left) // 2)
           if multiplier * potions[mid] >= success:
               right = mid - 1
           else:
               left = mid + 1

       return pn - left