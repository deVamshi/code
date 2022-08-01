class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        
        int i = nums.size() - 2;
        
        while(i > -1) {
            if(nums[i] < nums[i + 1])break;
            i--;
        }
        
        int ind = nums.size() - 1;
        
        while(ind > -1 && i >= 0){
            if(nums[ind] > nums[i]) break;
            ind--;
        } 
        
        if(i >= 0 && ind >= 0) 
            swap(nums[i], nums[ind]);
        
        reverse(nums.begin() + i + 1, nums.end());
        
    }
};