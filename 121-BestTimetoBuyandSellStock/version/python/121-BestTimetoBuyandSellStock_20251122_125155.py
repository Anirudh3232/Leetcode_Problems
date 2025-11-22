# Last updated: 11/22/2025, 12:51:55 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       l, r = 0, 1
       maxP = 0

       while r < len(prices):
        if prices[l] < prices[r]:
              profit = prices[r] - prices[l]
              maxP = max(maxP, profit)
        else:
             l = r
        r += 1

       return maxP
