class Solution:
    def myPow(self, x: float, n: int) -> float:
        self.temp = x
        @cache
        def pow(x,n):
            if n == 0:
                # print(1)
                return 1
            if n == 1:
                # print(x)
                return x
            if n == -1:
                return 1/x

            if n%2 == 0:
                return float(pow(x,n//2) ** 2)
            else:
                return self.temp * (pow(x,n//2) ** 2)
        
        return pow(x,n)