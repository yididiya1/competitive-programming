class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        spiral_matrix = [[0] * n for i in range(n)]
        start_value = 1
        spiral = n//2 + n%2
        
        
        
        for i in range(spiral):
            start,end = i , n-1-i
            if start == end:
                spiral_matrix[start][end] = start_value
            else:
                start_value = self.fillLayer(start,end,start_value,spiral_matrix)
            
        return spiral_matrix
        
        
        
    def fillLayer(self,start,end,start_value,matrix):

        start_row, end_row = start,end
        start_col, end_col = start,end
        
        #fill the top row
        for col in range(start_col,end_col):
            matrix[start_row][col] = start_value
            start_value += 1

        #fill the right column
        for row in range(start_row,end_row):
            matrix[row][end_col] = start_value
            start_value += 1

        #fill the bottom row
        for col in range(end_col,start_col,-1):
            matrix[end_row][col] = start_value
            start_value += 1

        #fill the left column
        for row in range(end_row,start_row,-1):
            matrix[row][start_col] = start_value
            start_value += 1

        return start_value
        
        
            
        
        
                
                
        
        