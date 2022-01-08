# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
class SolutionTow:
    def moveZeroes(self,nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        swappedIndex = 0
        for _ in range(len(nums)):
            if nums[swappedIndex] == 0:
                nums.pop(swappedIndex)
                nums.append(0)
            else:
                swappedIndex += 1