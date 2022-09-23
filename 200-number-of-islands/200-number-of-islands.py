class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.DIR = [[1,0],[0,1],[-1,0],[0,-1]]
        self.inBound = lambda row,col : 0 <= row < len(grid) and 0 <= col <len(grid[0]) 
        count = 0
        
        def dfs(row,col):
            grid[row][col] = "0"
            
            for r,c in self.DIR:
                new_row = row + r
                new_col = col + c
                if self.inBound(new_row,new_col) and grid[new_row][new_col] == '1':
                    dfs(new_row,new_col)
                    
                    
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row,col)
                    count += 1
                    
        return count
            
        