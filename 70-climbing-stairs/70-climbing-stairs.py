class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(nth):
            if nth == 0:
                return 1
            
            if nth == 1:
                return 1
            
            i = memo[nth-1] if nth-1 in memo else dp(nth-1)
            i_1 = memo[nth-2] if nth-2 in memo else dp(nth-2)
            
            
            memo[nth] = i + i_1
            
            return memo[nth]
        
        return (dp(n))