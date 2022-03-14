class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
       
    
        memo = {}
        
        
        def dp(row,index):
            # print(row,index)
            if row == len(triangle)-1:
                return triangle[row][index]
            
            
            _next = memo[(row+1,index)] if (row+1,index) in memo else dp(row+1,index)
            _next2 = memo[(row+1,index+1)] if (row+1,index+1) in memo else  dp(row+1,index+1)
            
            memo[(row,index)] = triangle[row][index]+min(_next,_next2)
            
            return memo[(row,index)]
        
        
        return (dp(0,0))
        