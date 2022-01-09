# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        minVal = prices[0]
        
        for val in prices:
            minVal = min(val, minVal)
            maxProfit = max(val - minVal, maxProfit)
            
        return maxProfit
            
class SolutionTwo:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            curP = prices[r] - prices[l]
            if curP > 0:
                maxP = max(curP, maxP)
            else:
                l = r
            r += 1
        return maxP
            
        