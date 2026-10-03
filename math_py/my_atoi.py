class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        MIN_INTEGER = -2 ** 31
        MAX_INTEGER = 2 ** 31 - 1
        numbers = []
        positive = False
        negative = False
        allowed_characters = {'+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

        for i in s:
            if i == '+' and positive:
                if not numbers:
                    return 0
                else:
                    break
            if i == '-' and negative:
                if not numbers:
                    return 0
                else:
                    break
            if i not in allowed_characters and not numbers:
                return 0
            if positive and negative:
                return 0
            if not i.isnumeric() and numbers:
                break
            if i == '-' and not numbers:
                negative = True
            if i == '+' and not numbers:
                positive = True
            if i.isdigit():
                numbers.append(i)

        result = 0

        for j in numbers:
            digit = ord(j) - ord('0')
            result = result * 10 + digit

        if negative:
            result = -result

        if result < MIN_INTEGER:
            result = MIN_INTEGER
        if result > MAX_INTEGER:
            result = MAX_INTEGER

        return result