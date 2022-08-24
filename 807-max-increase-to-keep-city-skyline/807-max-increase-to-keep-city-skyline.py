class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        tallest_row = {}
        tallest_col = {}
        
        
        for i in range(len(grid)):
            tallest_row[i] = max(grid[i])
        
        col = 0
        while col < len(grid):
            best = 0
            for i in range(len(grid)):
                best = max(best,grid[i][col])
            tallest_col[col] = best
            col += 1
            
        total = 0
        for row in range(len(grid)):
            for col in range(len(grid)):
                curr = grid[row][col]
                if curr == tallest_row[row] or curr == tallest_col[col]:
                    continue
                total += min(tallest_row[row],tallest_col[col]) - curr
                
        return total
                    
        