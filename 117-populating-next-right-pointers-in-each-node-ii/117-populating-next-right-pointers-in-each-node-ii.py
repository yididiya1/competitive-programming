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
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        dummy = Node(next = root)
        
        queue = deque()
        queue.append(root)
        
        while queue:
            cur = queue.popleft()
            n = len(queue)
            
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            
            if queue:
                for i in range(n):
                        x = queue.popleft()
                        if x.left:
                            queue.append(x.left)
                        if x.right:
                            queue.append(x.right)

                        cur.next = x
                        cur = x
            else:
                cur.next = None 
                
        
        return dummy.next
            
            
        
                
            
            
        
        