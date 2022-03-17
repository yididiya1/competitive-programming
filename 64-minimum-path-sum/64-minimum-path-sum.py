class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.inBound = lambda row,col: 0 <= row < len(grid) and 0 <= col < len(grid[0])
        self.directions = [[1,0],[0,1]]
        
        
        memo = {}
        
        def dp(row,col):
            
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return grid[row][col]
            
            _min = float('inf')
            
            for r,c in self.directions:    
                new_row = row + r
                new_col = col + c
                if self.inBound(new_row,new_col):
                    if (new_row,new_col) in memo:
                        _min = min(memo[(new_row,new_col)],_min)
                    else:
                        _min = min(dp(new_row,new_col),_min)
            
            memo[(row,col)] = _min+grid[row][col]      
            return memo[(row,col)]
        
        
        return (dp(0,0))
                    
        