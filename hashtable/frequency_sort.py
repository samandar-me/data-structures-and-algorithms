from typing import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        result = []
        for k, v in sorted(counter.items(), key=lambda item: item[1], reverse=True):
            for _ in range(v):
                result.append(k)

        return "".join(result)