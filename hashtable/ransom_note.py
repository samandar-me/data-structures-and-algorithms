from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter1 = Counter(ransomNote)
        counter2 = Counter(magazine)

        for s in ransomNote:
            c1 = counter1.get(s, -1)
            c2 = counter2.get(s, 0)
            if c1 > c2:
                return False

        return True