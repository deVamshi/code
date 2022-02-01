class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for ind in range(len(nums)):
            if target - nums[ind] in hashMap:
                return [ind, hashMap[target - nums[ind]]]
            hashMap[nums[ind]] = ind
        