class RandomizedCollection:

    def __init__(self):
        self.occurence = defaultdict(set)
        self.keys = []


    def insert(self, val: int) -> bool:
        result = len(self.occurence[val]) == 0
        
        self.occurence[val].add(len(self.keys))
        self.keys.append(val)
        
        return result
        
    def remove(self, val: int) -> bool:
        if len(self.occurence[val]) == 0:
            return False
        else:
            index = self.occurence[val].pop()
            if index == len(self.keys) -1:
                # self.occurence[self.keys[index]].remove(index)
                self.keys.pop()          
            else:
                self.occurence[self.keys[-1]].remove(len(self.keys)-1)
                self.occurence[self.keys[-1]].add(index)
                self.keys[-1],self.keys[index] = self.keys[index],self.keys[-1]
                self.keys.pop()
        return True    
    
    def getRandom(self) -> int:

        return random.choice(self.keys)
            


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()