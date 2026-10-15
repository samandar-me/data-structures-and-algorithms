class Solution:
    def countBits(self, n: int) -> list[int]:
        result = [0]
        for i in range(2, n + 1):
            bit_count = result[i>>1] + (i & 1)
            result.append(bit_count)

        return result

    # def countBits(self, n: int) -> list[int]:
    #     bits = []
    #
    #     for i in range(n + 1):
    #         bits.append(self.get_bit_count(i))
    #
    #     return bits
    #
    # def get_bit_count(self, n: int) -> int:
    #     count = 0
    #
    #     while n != 0:
    #         count += n & 1
    #         n >>= 1
    #
    #     return count