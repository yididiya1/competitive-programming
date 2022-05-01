from collections import Counter 


# class TrieNode:
#     def __init__(self):
#         self.isEnd = False
#         self.chars = {}

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#         self.freq = {}
    
#     def insert(self, word: str) -> None:
#         curr = self.root
#         for char in word:
#             if char not in curr.chars:
#                 curr.chars[char] = TrieNode()
#             curr = curr.chars[char] 
        
        
#         if curr.isEnd == True:
#             # print(self.freq)
#             self.freq[word] += 1
#         else:
#             self.freq[word] = 1
#         curr.isEnd = True
        
#     def getfreq(self) -> bool:
#         return self.freq
    
    
    
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        
        freq_dict = Counter(words)
        
        _maxHeap = [(-freq,element) for element , freq in freq_dict.items()]
        
        heapq.heapify(_maxHeap)
        
        
        return [heapq.heappop(_maxHeap)[1] for _ in range(k)]
        
#         trie = Trie()
#         count = 0
#         for word in words:
#             trie.insert(word)
        
#         _dict = trie.getfreq()
        
#         freq = [(_dict[word],word) for word in _dict]
        
#         freq.sort(reverse = True)
        
#         answer = sorted(freq,key = lambda x:(x[0],x[1]),reverse = True)
        
        
        
        
#         answer =  [freq[i] for i in range(k)]
       
#         # print(answer)
        
    
        
#         return answer
        
            
        
        
        
        

        
        
        