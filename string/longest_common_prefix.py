# Longest common prefix
#
# Find the longest common prefix in the given strings.
#
# If there is no common prefix, return "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Result: "fl"
#
# Example 2:
#
# Input: ["dog","racecar","car"]
# Result: ""


def longestCommonPrefix(words: list) -> str:
    if not words: return ""

    first_word = words[0]

    for i in range(len(first_word)):
        char = first_word[i]

        for j in range(1, len(words)):
            if i == len(words[j]) or words[j][i] != char:
                return first_word[:i]

    return first_word