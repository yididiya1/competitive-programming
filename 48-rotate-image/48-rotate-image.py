class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        left,right = 0,len(matrix)-1
        
        
        while left < right:
            top,bottom = left,right
            
            for i in range(right-left):
                
                #save topleft in temp
                temp = matrix[top][left+i]
                
                #rotate bottom-left ---> top-left
                matrix[top][left+i] = matrix[bottom-i][left] 
                
                #rotate bottom-right ---> bottom-left
                matrix[bottom-i][left] = matrix[bottom][right-i]
                
                #rotate top-right ---> bottom-right
                matrix[bottom][right-i] = matrix[top+i][right]
                
                #rotate top-left ----> top-right
                matrix[top+i][right] = temp
                
            left += 1
            right -= 1
        