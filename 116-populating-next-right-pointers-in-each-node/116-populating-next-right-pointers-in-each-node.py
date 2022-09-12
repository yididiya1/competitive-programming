"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return root
        
        queue = deque([root])
        
        while queue:
            prev = None
            for i in range(len(queue)):
                prev = queue.popleft()
                nxt = queue.popleft() if queue else None
                prev.next = nxt
                if prev.left:
                    queue.append(prev.left)
                if prev.right:
                    queue.append(prev.right)
                
                if nxt:
                    queue.appendleft(nxt)
            
            if prev:
                prev.next = None
            
        
            # print("=========")
            
         
            
        return root
            
        