# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        self.best = 0
        
        def dfs(node):
            if not node:
                return True,0,float('inf'),float('-inf')
            
            
            lValid,lsum,lmin,lmax = dfs(node.left)
            rValid,rsum,rmin,rmax = dfs(node.right)


            if lValid and rValid and lmax < node.val < rmin:
                self.best = max(self.best,lsum+rsum+node.val)
                return True,node.val+lsum+rsum,min(node.val,lmin),max(node.val,rmax)
            else:
                return False,0,float('inf'),float('-inf')

        
        dfs(root)
        return self.best
        