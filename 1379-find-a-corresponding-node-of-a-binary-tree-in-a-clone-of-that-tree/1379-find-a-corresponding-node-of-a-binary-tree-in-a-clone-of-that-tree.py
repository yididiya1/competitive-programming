# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        queue = deque()
        queue.append(cloned)
        
        
        while queue:
            x = queue.popleft()
            if x.val == target.val:
                return x
            
            if x.left:
                queue.append(x.left)
            
            if x.right:
                queue.append(x.right)
        
        