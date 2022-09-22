class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        
        @cache
        def dp(index,curr):
            if index >= len(nums):
                if curr == target:
                    return 1
                return 0
            
            
            
            pos = dp(index+1, nums[index] + curr)
            neg = dp(index+1,-nums[index] + curr)
            
            return pos+neg
        
        
        return dp(0,0)
            
            
            
        