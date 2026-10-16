from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        indexOfUnique = -1
        for i in range(len(s)):
            if counter.get(s[i], -1) == 1:
                indexOfUnique = i
                break

        return indexOfUnique