class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []: return 0
        mini = prices[0]
        maxP = float('-inf')
        for ele in prices:
            maxP = max(maxP, ele - mini)
            mini = min(ele, mini)
            
        return maxP
            
        