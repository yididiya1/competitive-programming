class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_col = 0
        r_col = len(matrix[0]) - 1
        l_row = 0
        r_row = len(matrix) - 1
        
        while  l_row <= r_row:
            mid_row = (l_row+r_row)//2
            
            
            if matrix[mid_row][0] <= target and matrix[mid_row][-1] >= target:
                while l_col <= r_col:
                    mid_col = (l_col+r_col)//2
                    if matrix[mid_row][mid_col] == target:
                        return True
                    elif matrix[mid_row][mid_col] > target:
                        r_col = mid_col-1
                    else:
                        l_col = mid_col+1
                return False                       
                            
                            
            if matrix[mid_row][0] > target:
                r_row = mid_row -1
            elif matrix[mid_row][-1] < target:
                l_row = mid_row +1
                
            
                    
        return False