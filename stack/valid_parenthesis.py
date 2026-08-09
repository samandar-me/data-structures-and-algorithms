
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"}": "{","]": "[", ")": "(" }

        for bracket in s:
            if bracket not in brackets:
                stack.append(bracket)
                continue

            if not stack: return False

            opening = stack.pop()

            if brackets[bracket] != opening:
                return False

        return len(stack) == 0
