class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        counter = 0
        k = 3
        sub_s = []
        right = 0

        while right < len(s):
            sub_s.append(s[right])
            if right - k >= 0:
                sub_s.remove(s[right-k])

            if len(set(sub_s)) == k:
                counter += 1

            right += 1


        return counter