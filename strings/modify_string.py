import string
import random

class Solution:
    def modifyString(self, s: str) -> str:
        word_list = list(s)
        length = len(word_list)

        for i in range(len(word_list)):
            if word_list[i] == "?":
                word_list[i] = self.get_char(word_list, i, length)

        return "".join(word_list)



    def get_char(self, word_list, i: int, length: int) -> str:
        letters = set(string.ascii_lowercase)

        if i > 0:
            letters.discard(word_list[i-1])

        if i < length - 1:
            right = word_list[i+1]
            if right == "?":
                return random.choice(list(letters))
            else:
                letters.discard(right)

        return random.choice(list(letters))