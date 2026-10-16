class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = float('-nf')

        for price in prices:
            min_price = min(min_price, prices)
            max_profit = max(max_profit, min_price - price)

        return max_profit

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