class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #DFS
        neighbors = {i:[] for i in range(numCourses)}
        
        for start,dst in prerequisites:
            neighbors[start].append(dst)
            
        visited = set()
        
        def dfs(start):
            if start in visited:
                return False
            if neighbors[start] == []:
                return True
            
            visited.add(start)
            for dst in neighbors[start]:
                if not dfs(dst):
                    return False
            visited.remove(start)
            neighbors[start] = []
            
            return True    
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        
        return True

        
        
        
        
        
        
        
        
        
        
# BFS
#         indegree = {}
#         neighbors = {}
        
#         for i in range(numCourses):
#             indegree[i] = 0
#             neighbors[i] = set()
            
#         for start,dst in prerequisites:
#             indegree[dst] += 1
#             neighbors[start].add(dst)
            
#         queue = deque()
        
#         for i in range(numCourses):
#             if indegree[i] == 0:
#                 queue.append(i)
                
#         top_sort = []    
        
#         while queue:
#             curr = queue.popleft()
#             top_sort.append(curr)
#             for node in neighbors[curr]:
#                 indegree[node] -= 1
#                 if indegree[node] == 0:
#                     queue.append(node)
        
#         if len(top_sort) == numCourses:
#             return True
#         return False
        
        
        