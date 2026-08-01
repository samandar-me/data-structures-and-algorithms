class Solution:
    def reverseWords(self, s: str) -> str:
        list_of_words = s.split(" ")
        result = []

        for char in list_of_words:
            if char != "":
                result.append(char)

        return " ".join(reversed(result))