class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        for i in range(len(cost)-3,-1,-1):
            cost[i] += min(cost[i+1],cost[i+2])
            
        return min(cost[0],cost[1])
        
    
#         memo = {}
        
#         def dp(index):
#             if index in memo:
#                 return memo[index]
            
#             if index == len(cost)-1:
#                 return cost[index]
#             if index == len(cost) -2:
#                 return min(cost[-1]+cost[-2],cost[-2])
            
            
# #             _next = memo[index+1] if index+1 in memo else dp(index+1)
# #             _nextnext = memo[index+2] if index+2 in memo else dp(index+2)
            
#             memo[index] = cost[index] + min(dp(index+1),dp(index+2))
            
#             return memo[index]
            
            
        
#         # print(dp(0),dp(1))
#         return min(dp(0),dp(1))
        
        
             
        
        
        