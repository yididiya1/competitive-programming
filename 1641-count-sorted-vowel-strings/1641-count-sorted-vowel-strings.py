class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        memo = {}
        
        def dp(n,last=''):
            if n == 0:
                return 1
            else:
            
                childsum = 0

                for i in ['a','e','i','o','u']:
                    if i >= last:
                        x = memo[(n-1,i)] if (n-1,i) in memo else dp(n-1,i)
                        childsum += x
                
                memo[(n,last)] = childsum
                return childsum
        
        return dp(n)