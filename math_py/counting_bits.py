from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        for i in range(n + 1):
            bits = self.convertBinaryAndCountOne(i)
            result.append(bits)

        return result

    def convertBinaryAndCountOne(self, n: int) -> int:
        counter = 0

        while n > 0:
            r = str(n % 2)
            if r == "1":
                counter += 1
            n //= 2

        return counter


