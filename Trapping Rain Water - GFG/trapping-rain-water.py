
class Solution:
    def trappingWater(self, arr,n):
        out = 0
        if len(arr) == 0: return out
        
        left = [] 
        right = [] 
        
        for ele in arr:
            if len(left) == 0: left.append(ele); continue;
            left.append(max(ele, left[-1]))
            
        for ele in reversed(arr):
            if len(right) == 0: right.append(ele); continue;
            right.append(max(ele, right[-1]))
            
            
        right = list(reversed(right))
        
        for ind in range(len(arr)):
            out += (min(left[ind], right[ind]) - arr[ind])
        
        return out
                
            
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends