class Solution:
    def fib(self, n: int) -> int:
        
        
        memo = {}
        
        def fibo(n):
            if n== 0:
                return 0
            elif n== 1:
                return 1
            else :
                prev = memo[n-1] if n-1 in memo else fibo(n-1)
                prevprev = memo[n-2] if n-2 in memo else fibo(n-2)
                
                memo[n] = prev+prevprev
                return prev + prevprev
        
        
        return fibo(n)
        