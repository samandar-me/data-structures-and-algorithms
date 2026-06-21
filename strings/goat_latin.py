VOWELS = "aeiouAEIOU"

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        result = []
        word_list = sentence.split()
        print(word_list)
        for i in range(len(word_list)):
            modified_word = self.transform_word(word_list[i], i+1)
            result.append(modified_word)

        return " ".join(result)

    def transform_word(self, word: str, index: int) -> str:
        if word[0] in VOWELS:
            return word + "ma" + (index * "a")

        return word[1:] + word[0] + "ma" + (index * "a")