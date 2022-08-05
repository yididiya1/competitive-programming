class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}
        
        
        def dp(_sum):
            if _sum in memo:
                return memo[_sum]
            
            if _sum == 0:
                return 1
            if _sum < 0:
                return 0
            
            x = 0
            for i in nums:
                x += dp(_sum-i)
            
            memo[_sum] = x 
            return x
        
        return dp(target)
            
        
        
        
        
        