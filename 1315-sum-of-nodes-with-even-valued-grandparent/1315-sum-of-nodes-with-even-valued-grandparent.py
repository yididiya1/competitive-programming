# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    
    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        self.total = 0
        
        def dfs(root,parent,grandparent):
            if not root:
                return 
            
            if grandparent and grandparent.val%2 == 0:
                self.total+=root.val
                
            dfs(root.left,root,parent)
            dfs(root.right,root,parent)
        
        
        
        dfs(root,None,None)
        return self.total
        