class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        self. DIR = [[0,1],[1,0]]
        self.inBound = lambda row,col:  1 <= row <= m  and 1 <= col <= n
        
        
        memo = {}
        
        def dp(row,col):
            if (row,col) == (m,n):
                return 1
            
            
            
            if (row,col) in memo:
                return memo[(row,col)]
            
            count = 0
            
            for r,c in self.DIR:
                new_row = row+r
                new_col = col+c
                if self.inBound(new_row,new_col):
                    count += dp(new_row,new_col)
            
            memo[(row,col)] = count
            return count
        
        return dp(1,1)
        
                
        