# https://leetcode.com/problems/find-the-duplicate-number/submissions/

# Python solution
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dupList = [0] * len(nums)
        for i in nums:
            if dupList[i] == 1: return i


# Java Solution
# class Solution {
#     public int findDuplicate(int[] nums) {
#         int[] arr = new int[nums.length];
#         Arrays.fill(arr, 0);
#         for(int i : nums){
#             if(arr[i] == 1) return i;
#             arr[i] = 1;
#         }
#
#         return 0;
#
#     }
# }
