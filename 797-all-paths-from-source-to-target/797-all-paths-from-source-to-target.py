class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        output = []
        
        def dfs(node,path):
            if node == len(graph) - 1:
                output.append(path)
                return 
                
            for n in graph[node]:
                x  = path.copy()
                x.append(n)
                dfs(n,x)
                
                
                
        dfs(0,[0])
        return output