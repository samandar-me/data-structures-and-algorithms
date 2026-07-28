class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = []

        length = min(len(word1), len(word2))

        for i in range(length):
            merged_string.append(word1[i])
            merged_string.append(word2[i])

        merged_string.extend(word1[length:])
        merged_string.extend(word2[length:])

        return "".join(merged_string)
