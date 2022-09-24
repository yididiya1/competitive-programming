class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        queue = deque([(0,0,k)])
        inBound = lambda row,col : 0 <= row < len(grid) and 0 <= col < len(grid[0])
        step  = 0
        visited = {}
        visited[(0,0)] = k
        
        while queue:
            # print(queue)
            n = len(queue)
            
            for i in range(n):
                row,col,left = queue.popleft()
                if (row,col) == (len(grid)-1,len(grid[0])-1):
                    return step
                for r,c in dirs:
                    new_r = row + r
                    new_c = col + c
                    if inBound(new_r,new_c):
                        if (new_r,new_c) not in visited or visited[(new_r,new_c)] < left :
                            if grid[new_r][new_c] == 1:
                                # print(new_r,new_c,"dede")
                                if left > 0:
                                    queue.append((new_r,new_c,left-1))
                                    visited[(new_r,new_c)] = left-1
                            else:
                                queue.append((new_r,new_c,left))
                                visited[(new_r,new_c)] = left
                            
            step += 1
            
        return -1
            
            
        
                        
        
        