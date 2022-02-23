class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        freq = {}
        
        for ele in nums1:
            freq[ele] = freq.get(ele, 0) + 1
                
        for ele in nums2:
            if ele in freq and freq[ele] > 0:
                out.append(ele)
                freq[ele] -= 1
        return out
        