"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root:
            return []
        
        queue = deque([root])
        output = []
        
        while queue:
            curr = []
            for i in range(len(queue)):
                x = queue.popleft()
                curr.append(x.val)
                for child in x.children:
                    queue.append(child)
            output.append(curr)
                    
        return output
                    
        