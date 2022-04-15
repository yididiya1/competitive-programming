# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return None
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if low <= node.val <= high:
                node.left = left
                node.right = right
                return node
            elif node.val < low:
                return right
            else:
                return left
        
        return dfs(root)
            
            
        
        
        