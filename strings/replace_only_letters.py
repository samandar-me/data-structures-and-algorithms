class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        result = list(s)

        left = 0
        right = len(s) - 1

        while left < right:
            if not result[left].isalpha():
                left += 1
                continue
            if not result[right].isalpha():
                right -= 1
                continue

            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1

        return "".join(result)
