VOWELS = {"a", "e", "i", "o", "u"}

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        window_size = 0
        answer = window_size

        left = 0
        right = k

        while right < len(s):
            if s[right] in VOWELS:
                window_size += 1
            if s[left] in VOWELS:
                window_size -= 1

            answer = max(answer, window_size)

            if answer == k:
                return k

            left += 1
            right += 1

        return answer


    # def maxVowels(self, s: str, k: int) -> int:
    #     window_size = self.count_vowels(s[:k])
    #
    #     answer = window_size
    #
    #     for right in range(k, len(s)):
    #         if s[right] in VOWELS:
    #             window_size += 1
    #         if s[right-k] in VOWELS:
    #             window_size -= 1
    #
    #         answer = max(answer, window_size)
    #
    #     return answer


    # def maxVowels(self, s: str, k: int) -> int:
    #     answer = self.count_vowels(s[:k])
    #
    #     left = 0
    #     right = k
    #
    #     while right <= len(s):
    #         counter = self.count_vowels(s[left:right])
    #         answer = max(answer, counter)
    #         left += 1
    #         right += 1
    #
    #
    #     return answer

    def count_vowels(self, s: str) -> int:
        count = 0

        for i in s:
            if i in VOWELS:
                count+=1

        return count