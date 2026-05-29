def removeStars(word: str) -> str:
    result = []

    for i in range(len(word)):
        current_str = word[i]

        if current_str != "*":
            result.append(current_str)
        else:
            result.pop()

    return "".join(result)