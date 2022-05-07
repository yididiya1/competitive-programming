class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #kmp solution O(n+m)
        if needle == "":
            return 0
        
        
        #build lps
        lps = [0] * len(needle)
        prevLps,i = 0, 1
        
        while i < len(needle):
            if needle[i] == needle[prevLps]:
                lps[i] = prevLps + 1
                prevLps += 1
                i += 1
            elif prevLps == 0:
                lps[i] = 0
                i += 1
            else:
                prevLps = lps[prevLps - 1]
                
                
        h , n = 0 , 0
        while h < len(haystack):
            if haystack[h] == needle[n]:
                n += 1
                h += 1
            else:
                if n == 0:
                    h += 1
                else:
                    n = lps[n-1]
                
            if n == len(needle):
                return h - len(needle)
            
        return -1