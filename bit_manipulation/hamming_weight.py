class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n != 0:
            count += n & 1
            n = n >> 1

        return count

    # def hammingWeight(self, n: int) -> int:
    #     weight = 0
    #     while n != 0:
    #         weight += n % 2
    #         n //= 2
    #
    #     return weight