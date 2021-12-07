# https://leetcode.com/problems/find-the-duplicate-number/submissions/

# Python solution
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dupList = [0] * len(nums)
        for i in nums:
            if dupList[i] == 1: return i

# Using floyds algorithm
# https://www.youtube.com/watch?v=wjYnzkAhcNk
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

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
