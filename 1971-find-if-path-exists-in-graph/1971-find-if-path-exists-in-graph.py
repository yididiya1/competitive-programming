class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        
        for start,dest in edges:
            graph[start].append(dest)
            graph[dest].append(start)
            
        visited = set()
        stack = [source]
        
        
        while stack:
            curr = stack.pop()
            
            if curr == destination:
                return True
            
            if curr in visited:
                continue
            
            visited.add(curr)
            
            for neigh in graph[curr]:
                stack.append(neigh)
        
        
        return False
        
        
        #recursive
#         def dfs(vert):
            
#             visited.add(vert)
            
#             if vert == destination:
#                 return True
            
#             me = False
#             for neighbor in graph[vert]:
#                 if neighbor not in visited:
#                     me = me or dfs(neighbor)
#             return me
            
#         return dfs(source)