class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_stock = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < lowest_stock:
                lowest_stock = prices[i]
            else:
                profit = prices[i] - lowest_stock
                if profit > max_profit:
                    max_profit = profit

        return max_profit