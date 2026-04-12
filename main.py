def longestPalindrome(text: str) -> str:
    if not text:
        return ""

    longest = ""

    for i in range(len(text)):
        odd_length = expand(text, i, i)
        event_length = expand(text, i, i + 1)

        longest = max([longest, odd_length, event_length], key=len)

    return longest

def expand(text, i, j) -> str:
    length = len(text)

    while i >= 0 and j < length and text[i] == text[j]:
        i -= 1
        j += 1

    return text[i+1: j]


if __name__ == '__main__':
    print(longestPalindrome("babad"))
