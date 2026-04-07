def detectCapitalUse(word: str) -> bool:
    if word.isupper() or word.islower():
        return True

    if not word:
        return False

    first_letter = word[0]
    remaining_letters = word[1:len(word)]
    return first_letter.isupper() and remaining_letters.islower()


if __name__ == '__main__':
    print(detectCapitalUse("FlaG"))