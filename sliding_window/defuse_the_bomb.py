from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)

        if k == 0:
            return [0] * n
        result = [0] * len(code)
        extended = code + code

        if k > 0:
            current_sum = sum(extended[1:k + 1])
        else:
            current_sum = sum(extended[k:])

        result[0] = current_sum

        if k > 0:
            for i in range(1, n):
                current_sum += extended[i + k]
                current_sum -= extended[i]
                result[i] = current_sum
        else:
            for i in range(1, n):
                current_sum += extended[i - 1]
                current_sum -= extended[(i - abs(k)) - 1]
                result[i] = current_sum

        return result