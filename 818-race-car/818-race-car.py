class Solution:
    def racecar(self, target: int) -> int:
        
        queue = deque([(0,1)])
        step = 0
        visited = set()
        visited.add((0,1))
        
        while queue:
            n = len(queue)
            for i in range(n):
                pos,speed = queue.popleft()
                if pos == target:
                    return step
                if speed > -1:
                    if (pos,-1) not in visited:
                        queue.append((pos,-1))
                        visited.add((pos,-1))
                else:
                    if (pos,1) not in visited:
                        queue.append((pos,1))
                        visited.add((pos,1))
                if (pos+speed,speed*2) not in visited:
                    queue.append((pos+speed,speed*2))
                    visited.add((pos+speed,speed*2))
            
            step += 1
                
        
        
                
                
                
        
        