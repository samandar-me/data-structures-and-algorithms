from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        answer = []
        k = len(p)
        p = Counter(p)
        window_count = Counter(s[:k])
        if window_count == p:
            answer.append(0)

        for right in range(k, len(s)):
            window_count[s[right]] += 1
            window_count[s[right-k]] -= 1
            if window_count == p:
                answer.append(right-k+1)

        return answer


    # def findAnagrams(self, s: str, p: str) -> list[int]:
    #     if len(p) > len(s):
    #         return []
    #
    #     answer = []
    #     pieces = []
    #     k = len(p)
    #     for i in range(len(s)-k+1):
    #         pieces.append(s[i:i+k])
    #
    #     p = Counter(p)
    #     for i in range(len(pieces)):
    #         if Counter(pieces[i]) == p:
    #             answer.append(i)
    #
    #     return answer

    # def findAnagrams(self, s: str, p: str) -> list[int]:
    #     ls = len(s)
    #     lp = len(p)
    #     if lp > ls:
    #         return []
    #
    #     answer = []
    #     p = "".join(sorted(p))
    #
    #     for i in range(ls):
    #         sorted_s = "".join(sorted(s[i:i+lp]))
    #         if sorted_s == p:
    #             answer.append(i)
    #
    #     return answer