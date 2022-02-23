class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for ele in nums:
            if ele in mp: return True
            mp[ele] = 0
        return False
        