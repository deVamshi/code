class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has = {}
        for i in range(len(nums)):
            req = target - nums[i]
            if req in has:
                out = [i, has[req]]
                return out
            else:
                has[nums[i]] = i
        print(has)

# https://leetcode.com/problems/two-sum/
