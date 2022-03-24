class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        finalA = {}
        l = 0
        r = 0
        result = []
        expected = 0
        
        if len(s) == 1:
            return [1]
        
        for i in range(len(s)):
            finalA[s[i]] = i
        
        
        # print(finalA)
        count = 0
        
        while r < len(s)-1:
            expected = max(finalA[s[l]],finalA[s[r]],expected)
            # print(l,r,result,expected)
            if r < expected:
                r += 1
            else:
                result.append(r-l+1)
                l = r+1
                r = r+1
        
        result.append(len(s)-l)        
        return (result)
                
        
        
                
                
        
        