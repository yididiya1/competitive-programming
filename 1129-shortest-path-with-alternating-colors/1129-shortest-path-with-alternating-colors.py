class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        min_path = [float('inf') for i in range(n)]
        
        graph_red = defaultdict(list)
        graph_blue = defaultdict(list)
        
        for start,dest in redEdges:
            graph_red[start].append(dest)
        
        for start,dest in blueEdges:
            graph_blue[start].append(dest)
            
        
        queue = deque([])
        queue.append((0,'',0))
        visited = {}
        
        while queue:
            # print(queue)
            node,last,step = queue.popleft()
            min_path[node] = min(min_path[node],step)
            visited[(node,last)] = step
            
            if last == 'R':
                # print("Here Red")
                for neigh in graph_blue[node]:
                    if (neigh,'B') not in visited: 
                        queue.append((neigh,'B',step+1))
                    elif (neigh,'B') in visited and visited[(neigh,'B')] > step+1:
                        queue.append((neigh,'B',step+1))
            elif last == 'B':
                # print("Here Blue")
                for neigh in graph_red[node]:
                    if (neigh,'R') not in visited: 
                        queue.append((neigh,'R',step+1))
                    elif (neigh,'R') in visited and visited[(neigh,'R')] > step+1:
                        queue.append((neigh,'R',step+1))
            else:
                for neigh in graph_blue[node]:
                    if (neigh,'B') not in visited: 
                        queue.append((neigh,'B',step+1))
                    elif (neigh,'B') in visited and visited[(neigh,'B')] > step+1:
                        queue.append((neigh,'B',step+1))
                
                for neigh in graph_red[node]:
                    if (neigh,'R') not in visited: 
                        queue.append((neigh,'R',step+1))
                    elif (neigh,'R') in visited and visited[(neigh,'R')] > step+1:
                        queue.append((neigh,'R',step+1))
                    
        
        for i in range(len(min_path)):
            if min_path[i] == float('inf'):
                min_path[i] = -1
                
        return min_path
            
            
        
        
        
        
        
        
        
        