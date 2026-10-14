class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0

        while max(x, y) != 0:
            distance += (x & 1) != (y & 1)
            x = x >> 1
            y = y >> 1

        return distance