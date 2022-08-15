class Solution:
    def romanToInt(self, s: str) -> int:
        
        
        digits = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        def rec(index):
            if index ==len(s)-1:
                return digits[s[index]]
        
            my_son = rec(index+1)
            me = digits[s[index]]
            
            if digits[s[index+1]] > me:
                return my_son-me
            else:
                return my_son+me
            
        return rec(0)
        
        
        