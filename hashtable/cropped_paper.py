def canConstruct(ransomNote: str, magazine: str) -> bool:

    for char in ransomNote:
        if contains(magazine, char):
            magazine = magazine.replace(char, "", 1)
            ransomNote = ransomNote.replace(char, "", 1)

    return len(ransomNote) == 0

def contains(magazine: str, char: str) -> bool:
    for i in magazine:
        if char == i:
            return True

    return False