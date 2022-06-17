class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        profit = 0
        minimum = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                profit = max(prices[i]-minimum, profit)
        return profit