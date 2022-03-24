class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        finalA = {}
        l,r = 0,0
        result = []
        expected = 0
        
        if len(s) == 1:
            return [1]
        
        for i in range(len(s)):
            finalA[s[i]] = i
     
        while r < len(s)-1:
            expected = max(finalA[s[l]],finalA[s[r]],expected)
            if r < expected:
                r += 1
            else:
                result.append(r-l+1)
                l = r+1
                r = r+1
        
        result.append(len(s)-l)        
        return (result)
                
        
        
                
                
        
        