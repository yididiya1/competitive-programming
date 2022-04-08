class NumMatrix:
    
    
    
    def __init__(self, matrix: List[List[int]]):
        
        for col in range(len(matrix[0])-1,-1,-1):
            for row in range(len(matrix)-2,-1,-1):
                matrix[row][col] += matrix[row+1][col]
        
        self.matrix = matrix
        
    def getRowSum(self,row,col1,col2):
        _sum = 0
        for i in range(col1,col2+1):
            _sum += self.matrix[row][i]
        return _sum
            

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sum = 0
        if row2 == len(self.matrix)-1:
            _sum = self.getRowSum(row1,col1,col2)
        else:
            _sum = self.getRowSum(row1,col1,col2) - self.getRowSum(row2+1,col1,col2)
            
        return _sum
            
            
            
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)