class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1

        while i >= 0 and s[i] == " ":
            i -= 1

        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length

    # def lengthOfLastWord(self, s: str) -> int:
    #     last_index = self.find_last_index(s)
    #     first_index = self.find_first_index(last_index, s)
    #
    #     return last_index - first_index + 1
    #
    # def find_first_index(self, last_index: int, s: str) -> int:
    #     for j in range(last_index, -1, -1):
    #         if s[j] == " ":
    #             return j + 1
    #
    #     return 0
    #
    # def find_last_index(self, s: str) -> int:
    #     for i in range(len(s) - 1, -1, -1):
    #         if s[i] != " ":
    #             return i
    #
    #     return 0