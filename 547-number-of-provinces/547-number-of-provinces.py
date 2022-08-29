class UnionByRank:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [0 for _ in range(size)]
        self.count = size
    def find(self,x):
        while x != self.root[x]:
            x = self.root[x]
        return x
    
    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[x] > self.rank[y]:
                self.root[rootY] = rootX
            elif self.rank[x] < self.rank[y]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1
    
    def getCount(self):
        return self.count
        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uc = UnionByRank(n)
        
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] == 1:
                    uc.union(i,j)
        return uc.getCount()
        
        
        