"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        self.clones = {}
        
        def clone(n):
            
            if n is None:
                return n
            
            
            if n in self.clones:
                return self.clones[n]
            
            cloned = Node(n.val,[])
            
            self.clones[n] = cloned
            
            neighbors = []
            for neigh in n.neighbors:
                neighbors.append(clone(neigh))
            
        
            cloned.neighbors = neighbors
            
            return cloned
        
        return clone(node)
            
            
        