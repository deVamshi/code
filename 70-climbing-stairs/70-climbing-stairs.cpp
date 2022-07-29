class Solution {
public:
    int cs(int n, unordered_map<int, int> &dp){
        if(dp.find(n) != dp.end()) return dp[n];
        if(n <= 0) return 0;
        else if(n <= 2) return n;
        else return dp[n] = cs(n - 1, dp) + cs(n - 2, dp);
        
    }
    
    int climbStairs(int n) {
        unordered_map<int, int> dp;
        return cs(n, dp);
    }
};