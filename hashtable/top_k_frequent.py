from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        repeat = 0
        result = []
        for key, _ in sorted(counter.items(), key=lambda item: item[1], reverse=True):
            if repeat == k:
                break
            result.append(key)
            repeat += 1

        return result