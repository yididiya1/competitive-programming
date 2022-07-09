class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashed = {}
        
        for x in strs:
            y = x
            x = list(x)
            x.sort()
            x = "".join(x)
            if x in hashed:
                hashed[x].append(y)
            else:
                hashed[x] = [y]
                
        
        return hashed.values()
        