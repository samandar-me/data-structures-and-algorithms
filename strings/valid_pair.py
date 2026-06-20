from collections import Counter

class Solution:
    def findValidPair(self, s: str) -> str:
        freq = Counter(s)

        for j in range(len(s) - 1):
            pair = s[j] + s[j + 1]
            p1 = freq.get(s[j], "")
            p2 = freq.get(s[j + 1], "")

            if p1 == p2:
                continue

            if pair == f"{p1}{p2}":
                return pair

        return ""

# def findValidPair(self, s: str) -> str:
#     map1 = {}
#     map2 = {}
#
#     for i in s:
#         map1[i] = 1 + map1.get(i, 0)
#
#     print(map1)
#
#     for k, v in map1.items():
#         if int(k) == v:
#             map2[k] = v
#
#     print(map2)
#
#     for j in range(len(s) - 1):
#         pair = s[j] + s[j+1]
#         p1 = map2.get(s[j], "")
#         p2 = map2.get(s[j+1], "")
#
#         if str(p1) == str(p2):
#             continue
#
#         if pair == f"{p1}{p2}":
#             return pair
#
#     return ""
