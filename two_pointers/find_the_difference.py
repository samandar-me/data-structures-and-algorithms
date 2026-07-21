from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_s = Counter(s)
        counter_t = Counter(t)

        for char, count in counter_t.items():
            if counter_s.get(char, 0) != count:
                return char

        return ""



    # def findTheDifference(self, s: str, t: str) -> str:
    #     if not s:
    #         return t
    #
    #     sorted_s = sorted(s)
    #     sorted_t = sorted(t)
    #
    #     sorted_s.append("#")
    #
    #     for i in range(len(sorted_s)):
    #         if sorted_s[i] != sorted_t[i]:
    #             return sorted_t[i]
    #
    #     return ""







