class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.Dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        self.in_bound = lambda row,col : 0 <= row < len(grid) and 0 <= col < len(grid[0])
        self.count = 0
        
        def dfs(r,c):
            grid[r][c] = 'X'
            
            for row,col in self.Dirs:
                new_r = r + row
                new_c = c + col
                
                if self.in_bound(new_r,new_c) and grid[new_r][new_c] != 0:
                    if grid[new_r][new_c] == 1:
                        dfs(new_r,new_c)
                else:
                    self.count += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i,j)
                    return self.count
                    # break
            # break
            
        # return self.count