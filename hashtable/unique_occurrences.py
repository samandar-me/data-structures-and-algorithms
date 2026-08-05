from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        seen = set()

        for value in counter.values():
            if value in seen:
                return False
            seen.add(value)

        return True