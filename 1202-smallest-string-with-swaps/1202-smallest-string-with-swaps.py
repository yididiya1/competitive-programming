class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [0 for i in range(size)]
    def find(self,x):
        while x != self.root[x]:
            x = self.root[x]
        return x
    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        s = list(s)
        uf = UnionFind(len(s))
        mapp = defaultdict(list)
        for start,end in pairs:
            uf.union(start,end)
        
        for i in range(len(s)):
            root = uf.find(i)
            mapp[root].append(i)
        
        for key in mapp:
            values = mapp[key]
            string = [s[i] for i in values]
            string.sort()
            pointer = 0
            for index in values:
                s[index] = string[pointer]
                pointer += 1
        
        return "".join(s)
        
        