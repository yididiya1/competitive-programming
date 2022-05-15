class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #top-down approach 
        
        memo = {}
        def dp(index):
            if index == 0:
                return nums[0]  
            if index == 1:
                return max(nums[0],nums[1])
            
            if index in memo:
                return memo[index]
            
            rob = dp(index-2) + nums[index]
            not_rob = dp(index - 1) + 0
            memo[index] = max(rob,not_rob)
            
            return memo[index]
        
        
        return dp(len(nums)-1)
        
        
        
        #bottom-up approach
        
        
        
        