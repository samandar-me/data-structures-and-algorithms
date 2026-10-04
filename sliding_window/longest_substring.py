class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        seen = set()
        n = len(s)

        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            window = (right - left) + 1
            longest = max(longest, window)
            seen.add(s[right])

        return longest