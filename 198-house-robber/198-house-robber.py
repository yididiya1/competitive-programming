class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def dp(index):
            if index >= len(nums):
                return 0
            
            rob = nums[index]+dp(index+2)
            not_rob = dp(index+1)
            
            return max(rob,not_rob)
        
        return dp(0)