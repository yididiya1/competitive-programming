# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return None
        
        largest  = {}
        queue = deque()
        queue.append((root,0))
        
        while queue:
            node,level = queue.popleft()
              
            largest[level] = max(largest[level],node.val) if level in largest else node.val
    
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))
        
        
        return largest.values()
                
            
        
        