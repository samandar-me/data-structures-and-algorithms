# Correct capitalization
#
# We consider the capitalization of a word to be correct in the following cases:
#
# Only the first letter is capitalized. For example, "Hello".
# No letters are capitalized. For example, "apple".
# All letters are capitalized. For example, "UZB".
# Check if the given word is capitalized correctly.
#
# Example 1:
#
# Input: word = "USA"
# Result: true
# Example 1:
#
# Input: word = "FlaG"
# Result: false

def detectCapitalUse(word: str) -> bool:
    if word.isupper() or word.islower():
        return True

    if not word:
        return False

    first_letter = word[0]
    remaining_letters = word[1:len(word)]
    return first_letter.isupper() and remaining_letters.islower()