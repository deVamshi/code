class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        
        int i;
        
        for(i = nums.size() - 2; i >= 0; i--){
            if(nums[i] < nums[i + 1]) break;
        }
        
        if(i == -1){
            reverse(nums.begin(), nums.end());
            return;
        }
        
        if (i > -1){
            int ind;
            for(ind = nums.size() - 1; ind > i; ind--){
                if(nums[ind] > nums[i]){
                    swap(nums[ind], nums[i]);
                    break;
                }
            }
        }
        reverse(nums.begin() + i + 1, nums.end());
    }
};