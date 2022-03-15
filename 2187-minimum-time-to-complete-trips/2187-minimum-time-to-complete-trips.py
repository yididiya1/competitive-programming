class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        time.sort()
        
        start = 0
        end = max(totalTrips,time[-1])*totalTrips
        result = float('inf')
        
        
        if totalTrips == 1:
            return time[0]
        
        while start <= end:
            mid = (start+end)//2
            count = 0
            for t in time:
                count += mid//t
            
            # print(count,mid)
            if count >= totalTrips:
                result = min(result,mid)
                end = mid-1
            else:
                start = mid+1
                
            
            
        return result
        
        
        
        