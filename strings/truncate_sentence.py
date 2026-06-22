class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        word_list = s.split()
        return " ".join(word_list[:k])

    # def kthSpace(self, s, k) -> int:
    #     for i in range(len(s)):
    #         word = s[i]
    #         if word == " " and i == k:
    #             return i
    #
    #     return 0
