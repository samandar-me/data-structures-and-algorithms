from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        largest = 0
        prefix = [0] * (n + 1)

        for i in range(n):
            current_altitude = prefix[i] + gain[i]
            prefix[i+1] = current_altitude
            largest = max(largest, current_altitude)

        return largest
