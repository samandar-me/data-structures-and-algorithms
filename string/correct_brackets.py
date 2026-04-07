# Correct brackets
#
# Check that the given brackets are placed correctly.
#
# Example 1:
#
# Input: "((()))"
#
# Result: true
#
# Example 2:
#
# Input: "(((""
#
# Result: false

def is_valid(s: str) -> bool:
    counter = 0

    for i in s:
        if i == "(":
            counter += 1
        elif i == ")":
            counter -= 1

        if counter < 0:
                return False

    return counter == 0