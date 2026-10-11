from typing import List

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digit = 0
        result = []

        for i in digits:
            digit = digit * 10 + i

        digit += 1
        while digit > 0:
            result.append(digit % 10)
            digit //= 10

        result.reverse()
        return result

    # def plusOne(self, digits: List[int]) -> List[int]:
    #     s_digits = (str(digits)
    #                 .replace(",", "")
    #                 .replace("[", "")
    #                 .replace("]", "")
    #                 .replace(" ", ""))
    #
    #
    #     result = []
    #     for i in str(int(s_digits) + 1):
    #         result.append(int(i))
    #
    #     return result
