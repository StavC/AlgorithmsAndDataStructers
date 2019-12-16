class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

'''
        min = 6666666
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            elif maxprofit < prices[i] - min:
                maxprofit = prices[i] - min
        return maxprofit
