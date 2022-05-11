class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        
        
        def dp(n,last=''):
            if n == 0:
                return 1
            else:
            
                childsum = 0

                for i in ['a','e','i','o','u']:
                    if i >= last:
                        childsum += dp(n-1,i)

                return childsum
        
        return dp(n)