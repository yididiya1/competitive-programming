class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        for i in range(len(cost)-3,-1,-1):
            cost[i] += min(cost[i+1],cost[i+2])
            
        return min(cost[0],cost[1])
        
#         @cache
#         def dp(index):
#             if index >= len(cost):
#                 return 0
#             return min(dp(index+1),dp(index+2))+cost[index]
        
#         return min(dp(0),dp(1))
    

        
             
        
        
        