
class Solution:
    def maxSubArraySum(self,arr,N):
        maxSum = float('-inf')
        currSum = 0
        for i in arr:
            currSum += i
            maxSum = max(currSum, maxSum)
            if currSum < 0: currSum = 0
        return maxSum































#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends