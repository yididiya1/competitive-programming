# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        self.prev = float('-inf') 
    
        def inOrder(node):
            if not node:
                return True
            
            w,x,y = True, False, True
            if node.left:
                w = inOrder(node.left)

            if node.val > self.prev:
                self.prev = node.val
                x = True

            if node.right:
                y = inOrder(node.right)
                
                
            return w and y and x
        
        
        return inOrder(root)
                    
            
        
        