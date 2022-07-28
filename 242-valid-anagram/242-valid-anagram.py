class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = Counter(s)
        t = Counter(t)
        
        if len(t) > len(s):
            s,t = t,s
        
        for i in s:
            if i not in t or s[i] != t[i] : return False
            
        return True
        
        