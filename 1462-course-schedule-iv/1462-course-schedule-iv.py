class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        n = numCourses
        
        dist = [[float('inf') for i in range(n)] for _ in range(n)]
        
        for start,end in prerequisites:
            dist[start][end] = 1
            
            
        
        # print(dist)
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
       
        
        # print(dist)
        return [dist[i][j] != float('inf') for i,j in queries]
            
        
        
                
            
        
        
        
        