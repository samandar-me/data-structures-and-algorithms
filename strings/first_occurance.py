class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1

        for i in range(len(haystack) - len(needle) + 1):
            sub_word = haystack[i:(i + len(needle))]

            if sub_word == needle:
                return i

        return -1