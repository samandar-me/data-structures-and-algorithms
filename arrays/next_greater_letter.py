class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        a = letters[0]
        letters = set(letters)
        all_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]

        target_index = all_letters.index(target)

        while target_index < len(all_letters):
            letter = all_letters[target_index]
            if letter in letters and letter != target:
                return letter
            target_index += 1

        return a