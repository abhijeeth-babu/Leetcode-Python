class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        current_min = prices[0]

        for price in prices:
            current_min = min(current_min, price)
            current_profit = price - current_min
            max_profit = max(max_profit, current_profit)

        return max_profit