class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        
        #top-down approach 
#         def dp(index):
#             if index == len(nums) - 1:
#                 return nums[index]
#             if index == len(nums) - 2:
#                 return max(nums[index+1],nums[index])
            
#             if index in memo : return memo[index]
            
#             rob = dp(index+2) + nums[index]
#             not_rob = dp(index+1) + 0
            
#             memo[index] = max(rob,not_rob)
            
#             return max(rob,not_rob)
        
#         return dp(0)
    
        #bottom-up appraoch
        
        if len(nums) == 1: return nums[0]
        
        nums[1] = max(nums[1],nums[0])
        
        for i in range(2,len(nums)):
            nums[i] = max((nums[i]+nums[i-2]),(nums[i-1]))
        
        # print(nums)
        return nums[-1]