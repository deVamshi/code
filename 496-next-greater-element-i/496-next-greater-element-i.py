class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        for ind, ele in enumerate(nums1):
            foundIndex = nums2.index(ele)
            for i in range(foundIndex + 1, len(nums2)):
                if nums2[i] > ele:
                    nums1[ind] = nums2[i]
                    break
            else:
                nums1[ind] = -1
                
        return nums1