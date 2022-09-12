class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        tickets.sort()
        
        graph = defaultdict(list)
        
        for start,end in tickets:
            graph[start].append(end)
        
        paths = ["JFK"]
        
       
        def dfs(location):
            
            if len(paths) == len(tickets)+1:
                return True
            
            if not graph[location]:
                return False
            
            
            temp = list(graph[location])
            for i,flight in enumerate(graph[location]):
                graph[location].pop(i)
                paths.append(flight)
                if dfs(flight):
                    return True
                graph[location].insert(i,flight)
                paths.pop()
                
            return False
                
                
        dfs("JFK")
        return paths