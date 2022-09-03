class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        self.output = []
        
        def dfs(num):
            if len(num) == n:
                self.output.append(num)
                return
            
            
            x = num[-1]
            possiblities = []
            if int(x) + k <= 9:
                possiblities.append(int(x)+k)
            if int(x) - k >= 0 and int(x)-k != int(x)+k:
                possiblities.append(int(x)-k)
            
            for pos in possiblities:
                a = num+str(pos)        
                dfs(a)
            
        for i in range(1,10):
            dfs(str(i))
            
        return self.output
        