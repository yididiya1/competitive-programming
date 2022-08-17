class Solution:
    def numTrees(self, n: int) -> int:
        
        @cache
        def dp(no):
            if no == 0 or no == 1:
                return 1
            
            my_sum = 0
            for i in range(1,no+1):
                my_sum += dp(i - 1)*dp(no-i)
            
            return my_sum
            
        return dp(n)
        
        