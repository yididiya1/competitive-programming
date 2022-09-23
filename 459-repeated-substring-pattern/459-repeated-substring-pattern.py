class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        pos = []
        for i in range(1,len(s)//2+1):
            if len(s)%i == 0 :
                    pos.append(i)

        for i in pos:
            chunks = [s[j:j+i] for j in range(0, len(s), i)]
            sample = chunks[0]
            if sample*len(chunks) == s:
                return True
            
        return False