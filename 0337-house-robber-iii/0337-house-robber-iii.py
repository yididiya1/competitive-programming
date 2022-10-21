# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0,0
           
            
            left_take,left_skip = dfs(node.left)
            right_take,right_skip = dfs(node.right)
            
            
            return left_skip+right_skip+node.val,max(left_take,left_skip)+max(right_take,right_skip)
            
        
        # print(dfs(root))
        return max(dfs(root))
            
            
            