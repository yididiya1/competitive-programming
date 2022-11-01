class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n = len(board)
        m = len(board[0])
        # dirs = [[0,1],[1,0]]
        self.inBound  = lambda row,col : 0 <= row < n and 0 <= col < m
        
        
        def dfs(row,col):
            
            board[row][col] = '.'
            
            if self.inBound(row,col+1) and board[row][col+1] == 'X':
                dfs(row,col+1)
            elif self.inBound(row+1,col) and board[row+1][col] == 'X':
                dfs(row+1,col)
                
        
        count = 0
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'X':
                    dfs(r,c)
                    count += 1
        
        return count
                    
        