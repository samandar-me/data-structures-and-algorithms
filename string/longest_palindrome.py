# Longest palindrome
#
# Find the longest palindrome in the given text. If there are 2 solutions ("bab", "aba") - return the first one ("bab").
#
# 💡 A palindrome is a word that is pronounced the same in reverse.
#
# Example 1:
#
# Input: "babad"
# Result: "bobo"
# Example 2:
#
# Input: "cbbd"
# Result: "bb"


def longestPalindrome(text: str) -> str:
	if not text:
		return ""

	longest = ""

	for i in range(len(text)):
		print(i)

	return longest