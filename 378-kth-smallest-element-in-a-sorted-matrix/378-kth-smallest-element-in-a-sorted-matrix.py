class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        
        _heap = []
        counter = 0
        _min = 0

        for i in range(len(matrix)):
            heapq.heappush(_heap,(matrix[i][0],i,0))     
            
        while counter < k:
            _min = heapq.heappop(_heap)
            if _min[2] != len(matrix)-1:
                heapq.heappush(_heap,(matrix[_min[1]][_min[2]+1],_min[1],_min[2]+1))
            counter += 1
            
            
        return _min[0]
                           
        
            
        
        
        
        