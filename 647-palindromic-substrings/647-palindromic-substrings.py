class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            
            for a, b in [(i, i), (i, i + 1)]:
                while a >= 0 and b < len(s) and s[a] == s[b]:
                    a -= 1
                    b += 1
                res += ((b - a - 1) + 1 ) // 2
                
        return res
                
            
        