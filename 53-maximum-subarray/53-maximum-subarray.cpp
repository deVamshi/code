class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        int maxi = INT_MIN;
        int curr = 0;
        
        for(int i : nums){
            curr += i;
            maxi = max(curr, maxi);
            if(curr <= 0) curr = 0;
        }
        
        return maxi;
        
    }
};