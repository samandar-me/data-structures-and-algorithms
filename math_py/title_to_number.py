def parse(letter) -> int:
    return ord(letter) - ord('A') + 1

def titleToNumber(columnTitle: str) -> int:
    res = 0

    for i, digit in enumerate(reversed(columnTitle)):
        res += parse(digit) * 26 ** i

    return res