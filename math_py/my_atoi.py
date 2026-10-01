class Solution:
    def myAtoi(self, s: str) -> int:
        MIN_INTEGER = -2**31
        MAX_INTEGER = 2**31-1
        nums = []

        return 0



    # def myAtoi(self, s: str) -> int:
    #     MIN_INTEGER = -2**31
    #     MAX_INTEGER = 2**31-1
    #     numbers = []
    #     positive = False
    #     negative = False
    #     allowed_characters = {' ', '+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    #
    #     for i in s:
    #         if i not in allowed_characters and not numbers:
    #             return 0
    #         if positive and negative:
    #             return 0
    #         if not i.isnumeric() and numbers:
    #             break
    #         if i == '0' and not numbers:
    #             continue
    #         if i == '-' and not numbers:
    #             negative = True
    #         if i == '+' and not numbers:
    #             positive = True
    #         if i.isdigit():
    #             numbers.append(i)
    #
    #     result = int(''.join(map(str, numbers)))
    #
    #     if result < MIN_INTEGER:
    #         result = MIN_INTEGER
    #     if result > MAX_INTEGER:
    #         result = MAX_INTEGER
    #
    #     if positive:
    #         return result
    #     if not positive and not negative:
    #         return result
    #
    #     return -result

    #Line 26: You are not allowed to use int() on a multi-character string created by joining the numbers list.