class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        short, long = sorted([nums1, nums2], key=len)
    
        for ele in short:
            for ind, same in enumerate(long):
                if same == ele:
                    out.append(ele)
                    long[ind] = "shit"
                    break
                
                
        return out
        