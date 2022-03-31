class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
       
    
        
    
#         memo = {}
        
        
#         def dp(row,index):
#             if row == len(triangle)-1:
#                 return triangle[row][index]
            
            
#             _next = memo[(row+1,index)] if (row+1,index) in memo else dp(row+1,index)
#             _next2 = memo[(row+1,index+1)] if (row+1,index+1) in memo else  dp(row+1,index+1)
            
#             memo[(row,index)] = triangle[row][index]+min(_next,_next2)
            
#             return memo[(row,index)]
        
        
#         return (dp(0,0))

        
        for arr in range(len(triangle)-2,-1,-1):
            for i in range(len(triangle[arr])):
                triangle[arr][i] +=  min(triangle[arr+1][i+1],triangle[arr+1][i])
                
        return (triangle[0][0])
                
                
            

        