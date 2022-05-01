

class Node:
    def __init__(self):
        self.isEnd = False
        self.chars = defaultdict(Node)

class Trie:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            # if char not in curr.chars:
            #     curr.chars[char] = Node()
            curr = curr.chars[char] 
        
        curr.isEnd = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.chars:
                return False
            curr = curr.chars[char] 
          
        return curr.isEnd
    
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.chars: 
                return False
            else:
                curr = curr.chars[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)