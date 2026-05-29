def findWords(words: list) -> set:
    result = set()

    rows = [
        set("qwertyuiopQWERTYUIOP"),
        set("asdfghjklASDFGHJKL"),
        set("zxcvbnmZXCVBNM"),
    ]

    for row in rows:
        for word in words:
            diff = set(word) - row
            if(len(diff)) == 0:
                result.add(word)

    return result