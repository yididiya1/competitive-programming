# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        self.ins = TreeNode(val)
        
        if not root:
            return self.ins 
        
        def insert(node):
            
            if not node:
                return
            
            if node.val > val:
                if node.left:
                    insert(node.left)
                else:
                    node.left = self.ins
            else:
                if node.right:
                    insert(node.right)
                else:
                    node.right = self.ins
                    
            
                    
        
        insert(root)
        return root
        
        
                
                
            
        