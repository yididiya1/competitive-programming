# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        ins = TreeNode(val)
        
        if not root:
            return ins 
        
        cur = root
        
        while True:
            if cur.val < val:
                #insert to the right
                if cur.right != None:
                    cur = cur.right
                else:
                    cur.right = ins
                    break
            else:
                #insert to left
                if cur.left != None:
                    cur = cur.left
                else:
                    cur.left = ins
                    break 
        return root
        
        
                
                
            
        