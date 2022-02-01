#User function Template for python3

class Solution:
    def factorial(self, N):
        memo = {}
        def fact(n):
            if n < 2:
                return 1
            else:
                if n in memo:
                    return memo[n]
                else:
                    memo[n] = n * fact(n - 1)
                    return memo[n]
                    
    
        return [fact(N)]
        
        
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N);
        for i in ans:
            print(i,end="")
        print()
    
# } Driver Code Ends