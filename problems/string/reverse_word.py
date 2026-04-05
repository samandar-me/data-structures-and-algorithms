# Reverse word
#
# Reverse the given list of characters.
#
# Let the memory complexity be O(1).
#
# Example 1:
#
# Input: s = ["h","e","l","l","o"]
# Result: ["o","l","l","e","h"]
# Example 2:
#
# Input: s = ["H","a","n","n","a","h"]
# Result: ["h","a","n","n","a","H"]

def reverseString(s: list) -> list:
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s