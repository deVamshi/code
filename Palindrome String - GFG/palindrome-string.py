#User function Template for python3
class Solution:
	def isPalindrome(self, S):
	    
	    start, end = 0, len(S) - 1
	    
	    while start < end:
	        if S[start] != S[end]: return 0
	        start, end = start + 1, end - 1
	        
	    return 1
	        
	   
		# code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends