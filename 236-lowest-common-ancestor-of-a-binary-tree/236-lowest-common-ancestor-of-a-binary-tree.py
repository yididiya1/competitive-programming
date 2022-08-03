# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node,p,q):
            
            if not node:
                return None
            
            if node == p or node == q:
                return node
            
            # if not node:
            #     return False
            
            
            left = dfs(node.left,p,q)
            right = dfs(node.right,p,q)
            
            if left  and right :
                return node
            
            return left or right
        
        return dfs(root,p,q)
            
        
        