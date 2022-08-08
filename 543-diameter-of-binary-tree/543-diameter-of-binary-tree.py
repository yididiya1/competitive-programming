# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.max = 0
        
        def lengthCalc(node):
            if not node:
                return 0
            
            left = lengthCalc(node.left)
            right = lengthCalc(node.right)
            
            self.max = max(self.max,left+right)
            me = max(left,right)+1
            
            return me
        
        lengthCalc(root)
        return self.max
        