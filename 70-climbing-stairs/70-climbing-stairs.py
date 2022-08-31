class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def dp(nth):
            if nth > n:
                return 0
            if nth == n:
                return 1
            one = dp(nth+1)
            two = dp(nth+2)
            return one + two
        
        return dp(0)