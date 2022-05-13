class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def f(ind):
            if ind == 0: return nums[ind]
            if ind < 0: return 0
            if ind in dp: return dp[ind]
            pick = nums[ind]
            if ind > 1: pick += f(ind - 2)
            notPick = 0 + f(ind - 1)
            
            dp[ind] = max(pick, notPick)
            return dp[ind]
        
        return f(len(nums) - 1)
            
        