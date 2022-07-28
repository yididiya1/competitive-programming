class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #check_row
        def check_row(row):
            check = set()
            for i in row:
                if i == '.':
                    continue
                else:
                    if i in check:
                        return False
                    else:
                        check.add(i)
            return True
        
        def check_col(index):
            check = set()
            for i in range(9):
                # print(board[i][index],"Checking Col ",i)
                if board[i][index] == '.':
                    continue
                else:
                    if board[i][index] in check:
                        return False
                    else:
                        check.add(board[i][index])
            return True
        
        def check_grid(topL,topR,bottomL,bottomR):
            check = set()
            for row in range(topL,topR+1):
                for col in range(bottomL,bottomR+1):
                    if board[row][col] == '.':
                        continue
                    else:
                        if board[row][col] in check:
                            return False
                        else:
                            check.add(board[row][col])
                        
            return True
        
        
        for i in range(9):
            x = check_row(board[i])
            y = check_col(i)
            if x == False or y == False : 
                # print("Row or Col Error",x,y,i)
                return False
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                x = check_grid(i,i+2,j,j+2)
                if x == False: 
                    print("Gird Error")
                    return False
        
        return True
                
            
        