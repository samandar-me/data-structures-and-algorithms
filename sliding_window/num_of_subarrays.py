from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counter = 0
        window_sum = 0

        for right in range(len(arr)):
            window_sum += arr[right]

            if right - k >= 0:
                window_sum -= arr[right - k]

            if right >= k - 1 and window_sum / k >= threshold:
                counter += 1

        return counter


