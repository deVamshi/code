class Solution {
public:
    int f(vector<int> &nums,int ind, vector<int> &dp){
        
        int ans = 1;
        
        if(dp[ind] != -1) return dp[ind];
        
        for(int j = 0; j < ind; j++){
            if(nums[ind] > nums[j]){
                ans = max(ans, 1 + f(nums, j, dp));
            }
        }
        
        return dp[ind] = ans;
    }
    
    int lengthOfLIS(vector<int>& nums) {
        
        vector<int> dp(nums.size() + 1, -1);
        
        int ans = 0;
        
        for(int i = 0; i < nums.size(); i++){
            ans = max(ans, f(nums, i, dp));
        }
        
        return ans;
    }
};