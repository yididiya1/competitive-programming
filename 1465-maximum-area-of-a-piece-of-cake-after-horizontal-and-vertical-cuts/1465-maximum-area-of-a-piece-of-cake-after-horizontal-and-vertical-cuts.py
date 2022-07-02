class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        
        horizontalCuts.sort()
        
        lastH = h - horizontalCuts[-1] 
        firstH = horizontalCuts[0] - 0
        
        
        for i in range(len(horizontalCuts)-1,0,-1):
            horizontalCuts[i] = horizontalCuts[i] - horizontalCuts[i-1]
        
        horizontalCuts[0] = firstH
        horizontalCuts.append(lastH)
        
        
        verticalCuts.sort()
        
        lastV = w - verticalCuts[-1] 
        firstV = verticalCuts[0] - 0
        
        
        for i in range(len(verticalCuts)-1,0,-1):
            verticalCuts[i] = verticalCuts[i] - verticalCuts[i-1]
        
        verticalCuts[0] = firstV
        verticalCuts.append(lastV)
        
        return (max(horizontalCuts) * max(verticalCuts))%(10**9 + 7)
        
        