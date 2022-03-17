class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        
        if len(nums) == 1:
            return nums[0]
        
        
        nums[1] = max(nums[0],nums[1])
        
        
        
        for i in range(2,len(nums)):
            nums[i] = max(nums[i-2]+nums[i],nums[i-1]) 
            
            
        return max(nums)
                
        
        
        
        
        
        
        
        
        
        
#         def dp(index):
#             if index == len(nums)-1 :
#                 return nums[index]
#             if index == len(nums) -2:
#                 return min(nums[-2],nums[-1])
            
#             return min(nums(index),dp(index+1))
        
#         print(dp(0),dp(1))