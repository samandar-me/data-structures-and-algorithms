from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s_digits = (str(digits)
                    .replace(",", "")
                    .replace("[", "")
                    .replace("]", "")
                    .replace(" ", ""))


        result = []
        for i in str(int(s_digits) + 1):
            result.append(int(i))

        return result
