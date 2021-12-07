

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float('inf')
        profit = 0
        for i in prices:
            mini = min(i, mini)
            profit = max(profit, i - mini)
        return profit


# JAVA Solution
# class Solution {
#     public int maxProfit(int[] prices) {
#         int profit = 0;
#         int mini = Integet.MAX_VALUE;
#         for(int i : prices){
#             mini = i < mini ? i : mini;
#             profit = i - mini > profit ? i - mini : profit;
#         }
#         return profit;
#     }
# }
