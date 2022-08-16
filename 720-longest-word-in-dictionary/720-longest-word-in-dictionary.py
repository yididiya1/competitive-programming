class TrieNode:
    def __init__(self,val=""):
        self.children = {}
        self.isEnd = False
        self.val = val

class Solution:
    def longestWord(self, words: List[str]) -> str:
        self.root = TrieNode()
        
        
        def insert(word):
            curr = self.root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode(char)
                curr = curr.children[char]
            curr.isEnd = True
        
        for word in words:
            insert(word)
            
        def dp(node):
            if not node.children:
                return node.val
            
            
            _max = 0
            cmax = ""
            for child in node.children:
                mychild = node.children[child]
                if mychild.isEnd:
                    rchild = dp(mychild)
                    if len(rchild) > _max:
                        cmax = rchild
                        _max = len(cmax)
                    elif len(rchild) == _max:
                        if rchild[0] < cmax[0]:
                            cmax = rchild
                    
            
            return node.val+cmax
        
        return dp(self.root)
                
             