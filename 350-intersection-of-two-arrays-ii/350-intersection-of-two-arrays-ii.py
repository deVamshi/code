class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        short = []
        long = []
        out = []
        if len(nums1) < len(nums2):
            short = nums1
            long = nums2
        else:
            short = nums2
            long = nums1
        
        
        for ele in short:
            for ind, same in enumerate(long):
                if same == ele:
                    out.append(ele)
                    long[ind] = "shit"
                    break
                
                
        return out
        