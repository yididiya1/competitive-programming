class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # neighbors = {i:[] for i in range(len(graph))}
        output = []
        visited = set()
        memo = {}
        
        def dfs(idx):
            if idx in memo:
                return memo[idx]
            if idx in visited:
                return False
            if graph[idx] == []:
                return True
            
            visited.add(idx)
            for i in graph[idx]:
                answer = memo[i] if i in memo else dfs(i)
                if answer == False:
                    return False
            
            memo[idx] = True
            visited.remove(idx)
            return True
            
                    
        for i in range(len(graph)):
            if dfs(i) == True:
                output.append(i)
            
        return (output)
                    
            
            