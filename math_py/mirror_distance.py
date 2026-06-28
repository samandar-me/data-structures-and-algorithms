class Solution:
    def mirrorDistance(self, n: int) -> int:
        r = str(n)[::-1]
        return abs(n - int(r))

    # def mirrorDistance(self, n: int) -> int:
    #     return abs(n - self.reverse_number(n))
    #
    # def reverse_number(self, n: int) -> int:
    #     total = ""
    #
    #     while n > 0:
    #         total += str(n % 10)
    #         n //= 10
    #
    #     return int(total)