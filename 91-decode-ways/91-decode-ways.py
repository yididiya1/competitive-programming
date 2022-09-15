class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def dp(index):
            if index >= len(s):
                return 1 
            
            if s[index] == '0':
                return 0
            
            one = dp(index+1)
            two = dp(index+2) if index+1 < len(s) and int(s[index:index+2]) <= 26 else 0 
            
            return one+two
            
        
        return dp(0)