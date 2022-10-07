class Solution:
    def longestPalindrome(self, s: str) -> str:
        

#         self.best = [0,0,1]
#         self.memo = {}
#         def dp(l,r):
#             if (l,r) in self.memo: return self.memo[(l,r)]
#             if l > r: return True
#             check = False
#             if s[l] == s[r]:
#                 check = True and dp(l+1,r-1)
            
#             dp(l+1,r)
#             dp(l,r-1)
            
#             if check and (r - l + 1 ) > self.best[2]:
#                 self.best = [l,r,(r-l+1)]
            
#             self.memo[(l,r)] = check
#             return check
            
        
#         dp(0,len(s)-1)
#         return s[self.best[0]:self.best[1]+1]
        
        best = [0,0,0]
        for i in range(len(s)):
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > best[2]:
                    best = [l,r,r-l+1]
                l -= 1
                r += 1
                
            
            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > best[2]:
                    best = [l,r,r-l+1]
                l -= 1
                r += 1
                
        return s[best[0]:best[1]+1]
                
                