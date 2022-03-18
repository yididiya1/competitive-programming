class Solution:
    def tribonacci(self, n: int) -> int:
        
        memo = {}
        
        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            if i == 2:
                return 1
            
            i_1 = memo[i-1] if i-1 in memo else dp(i-1)
            i_2 = memo[i-2] if i-2 in memo else dp(i-2)
            i_3 = memo[i-3] if i-3 in memo else dp(i-3)
            
            memo[i] = i_1+i_2+i_3
            return memo[i]
        
        return dp(n)
        