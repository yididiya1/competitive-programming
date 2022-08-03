class RandomizedSet:

    def __init__(self):
        self.ratio = {}
        self.list = []
    def insert(self, val: int) -> bool:
        if val in self.ratio and self.ratio[val] == 1:
            return False
        self.list.append(val)   
        self.ratio[val] = 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.ratio or self.ratio[val] == 0:
            return False
        self.ratio[val] = 0
        return True

    def getRandom(self) -> int:
        
        while True:
            randonNo = random.randint(0,len(self.list)-1)
            if self.ratio[self.list[randonNo]] == 1:
                return self.list[randonNo]
            
            

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()