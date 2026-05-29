brackets = {
    "}": "{",
    "]": "[",
    ")": "(",
}


def isValid(word: str) -> bool:
    stack = []

    for bracket in word:
        if bracket not in brackets: # keys
            print(bracket)
            stack.append(bracket)
            continue

        if not stack: return False

        closing = bracket
        opening = stack.pop()

        if brackets[closing] != opening:
            return False

    return len(stack) == 0
