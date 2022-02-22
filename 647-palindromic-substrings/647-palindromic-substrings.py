class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for ind in range(len(s)):
            l = r = ind
            
            while l > -1 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
                
            l = ind
            r = ind + 1
            
            while l > -1 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
                
        return res
            
        