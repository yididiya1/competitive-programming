# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.count = 0
        
        def dfs(node,_max):
            if not node:
                return
            
            if node.val >= _max:
                self.count += 1
                _max = node.val
            
            left = dfs(node.left,_max)
            right = dfs(node.right,_max)
            
        dfs(root,float('-inf'))
        
        return self.count
            
            