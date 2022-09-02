# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        queue = deque()
        result = []
        queue.append((root,0))
        
        while queue:
            
            size = len(queue)
            _sum = 0
            _count = 0
            
            for i in range(size):
                current,level = queue.popleft()
                _count += 1
                _sum += current.val
                
                if current.left:
                    queue.append((current.left,level+1))
                
                if current.right:
                    queue.append((current.right,level+1))
            
           
            result.append(_sum/_count)
            
            
        
        return (result)
            
            
        
        
        
        