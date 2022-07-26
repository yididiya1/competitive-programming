class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        
        def check_speed(speed):
            
            total = 0
            
            for i in piles:
                total += ceil(i/speed)
            
            return total
        
        best = float('inf')
        
        high = max(piles)
        low = 1 
        
        # print(low,high)
        
        while low <= high:
            
            mid = (low+high)//2
            answer = check_speed(mid)
            
            # print(low,high,mid,answer)
            
            if answer <= h:
                best = min(best,mid)
                high = mid - 1
            else :
                low = mid + 1
            # else:
            #     high = mid - 1
                
        
        return best  
        