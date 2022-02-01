#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        out = 0
        hashMap = {}
        for ind, ele in enumerate(arr):
            if ele in hashMap:
                hashMap[ele].append(ind)
            else:
                hashMap[ele] = [ind]
                
        out = 0
        
        for ind, ele in enumerate(arr):
    
            if k - ele in hashMap:
                for index in hashMap[k - ele]:
                    if index > ind:
                        out += 1
                        
        return out
                        
                    
                
        # for ind in range(len(arr)):
        #     out += arr[ind + 1:].count(k - arr[ind])
        # return out
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends