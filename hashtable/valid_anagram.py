class Solution:

    def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        diff = set(s) - set(t)
        return len(diff) == 0

    # def isAnagram(s: str, t: str) -> bool:
    #     return Counter(s) == Counter(t)

    # def isAnagram(s: str, t: str) -> bool:
    #     # If lengths are different, they cannot be anagrams
    #     if len(s) != len(t):
    #         return False
    #
    #     countS, countT = {}, {}
    #
    #     # Build frequency maps
    #     for i in range(len(s)):
    #         countS[s[i]] = 1 + countS.get(s[i], 0)
    #         countT[t[i]] = 1 + countT.get(t[i], 0)
    #
    #     return countS == countT

    # def isAnagram(self, s: str, t: str) -> bool:
    #     return sorted(t) == sorted(s)

    # - Wrong solution
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return self.calculate_sum(t) == self.calculate_sum(s)

    # def calculate_sum(self, word: str) -> int:
    #     sum_ = 0
    #
    #     for i in range(len(word)):
    #         sum_ += ord(word[i])
    #
    #     return sum_