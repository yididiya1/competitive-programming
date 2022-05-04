class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        neighbors = { i:[] for i in range(len(graph))}
        indegree = [len(i) for i in graph]
        queue = deque()
        
        
        # print(indegree)
        
        for i in range(len(graph)):
            for num in graph[i]:
                neighbors[num].append(i)
        
        # print(neighbors)
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        
        # print(queue)
        
        output = []
        
        
        while queue:
            index = queue.popleft()
            output.append(index)
            
            for num in neighbors[index]:
                indegree[num] -= 1
                if indegree[num] == 0:
                    queue.append(num)
                    
        output.sort()
        
        return output
            
        