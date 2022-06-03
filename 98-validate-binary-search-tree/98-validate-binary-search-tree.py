# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        
        def isValid(node,lb,rb):
            if not node:
                return True
            if not ( lb < node.val and node.val < rb):
                return False
            
            leftSubTree = isValid(node.left,lb,node.val)
            rightSubTree = isValid(node.right,node.val,rb)
            
            return leftSubTree and rightSubTree
           
        
        return isValid(root,float('-inf'),float('inf'))
                    
            
        
        