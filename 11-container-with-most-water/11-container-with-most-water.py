class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l = 0
        r = len(height)  - 1
        
        current_max = (r-l) * min(height[r],height[l])
        
        while l < r:
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1     
            current_max = max(current_max,(r-l) * min(height[r],height[l]))
            
        return current_max
            
                
            
                
                
            
        
        