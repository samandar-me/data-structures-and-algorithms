class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = float('-inf')
        left = 0
        right = len(prices) - 1

        while left < right:
            max_profit = max(max_profit, (prices[right] - prices[left]))
            if prices[left + 1] < prices[left]:
                left += 1
            elif prices[right-1] > prices[right]:
                right -= 1
            else:
                if prices[left] < prices[right]:
                    left += 1
                else:
                    right -= 1

        return int(max_profit) if max_profit > 0 else 0

    # def maxProfit(self, prices: list[int]) -> int:
    #     max_profit = float('-inf')
    #     left = 0
    #     right = len(prices) - 1
    #
    #     while left <= right:
    #         max_profit = max(max_profit, (prices[right] - prices[left]))
    #         if prices[left] < prices[right]:
    #             left += 1
    #         else:
    #             right -= 1
    #
    #     return int(max_profit)