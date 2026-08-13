class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0

        for c in s:
            if c not in seen:
                seen.add(c)
            else:
                longest = max(longest, len(seen))
                seen = set()
                seen.add(c)

        return max(longest, len(seen))