#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
	    out = []
	    
	    for i in range(1, 1 << len(s)):
	        
	        curr = ""
	        
	        for j in range(len(s)):
	            
	            if i & (1 << j): curr += s[j]
	            
	        out.append(curr)
	        
	    return sorted(out)
	    
	    
		# Code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends