class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        queue = deque()
        queue.append(start)
        self.inBound = lambda index : 0 <= index < len(arr)
        visited = set()
        
        while queue:
            element = queue.popleft()
            visited.add(element)
            if arr[element] == 0:
                return True
                
            
            moves = [element + arr[element],element - arr[element]]
            
            for m in moves:
                if self.inBound(m) and m not in visited:
                    queue.append(m)
                    
        return False
            
        
            
            
            
            
        
        
        
        