class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        buy, sell = 0, 0

        while sell < len(prices):
            profit = prices[sell] - prices[buy]

            maxProfit = max(maxProfit, profit)

            if prices[sell] < prices[buy]:
                buy = sell
            sell += 1
        return maxProfit
        