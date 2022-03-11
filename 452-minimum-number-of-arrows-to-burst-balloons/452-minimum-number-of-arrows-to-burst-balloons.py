class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        # print(points)
        count = 1
        
        curr_last = points[0][1]
        curr_start = points[0][0]
        
        
        for i in range(1,len(points)):
            start , end = points[i]
            if curr_start <= start <= curr_last:
                curr_last = min(end,curr_last)
                curr_start = max(start,curr_start)
            else:
                count += 1
                curr_last = end
                curr_start = start
                
        return (count)
        