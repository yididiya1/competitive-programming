class Solution:
    def reverseWords(self, s: str) -> str:
        
        
        def reverseWord(word):
            word = list(word)
            l = 0
            r = len(word)-1
            
            while l < r:
                word[l],word[r] = word[r],word[l]
                l += 1
                r -= 1
            
            return word
        
        s= s.split(" ")
        s = ["".join(reverseWord(w)) for w in s]
        return " ".join(s)
        
        
        
        
        