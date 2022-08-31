class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        neighbors = {i:[] for i in range(numCourses)}
        queue = deque()
        indegree = {i:0 for i in range(numCourses)}
        
        for start,dst in prerequisites:
            neighbors[dst].append(start)
            indegree[start] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        
        top_sort  = []
        
        while queue:
            start = queue.popleft()    
            top_sort.append(start)
            for dst in neighbors[start]:
                indegree[dst] -= 1
                if indegree[dst] == 0:
                    queue.append(dst)
        
        if len(top_sort) == numCourses:
            return top_sort
        return []    

#         neighbors = { i : [] for i in range(numCourses)}
#         visited = set()
#         added = set()
        
        
#         top_sort = []
        
#         for start,dst in prerequisites:
#             neighbors[start].append(dst)
            
#         def dfs(start):
#             if start in visited:
#                 return False
#             if start in added:
#                 return True
                
#             visited.add(start)
            
#             for dst in neighbors[start]:
#                 if not dfs(dst):
#                     return False
            
#             visited.remove(start)
#             added.add(start)
#             top_sort.append(start)
            
#             return True
            
#         for i in range(numCourses):
#             if dfs(i) == False:
#                 return []
            
#         return top_sort
            
            
        
        
        