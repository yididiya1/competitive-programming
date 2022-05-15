# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        
        queue = deque()
        queue.append(root)
        
        
        while queue:
            n = len(queue)
            layersum = 0
            
            for i in range(n):
                x = queue.popleft()
                layersum += x.val
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
            
            total = layersum
            
            
        return layersum
                
                
            
            
            
        