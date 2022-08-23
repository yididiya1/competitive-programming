# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
            self.idx = 0
            def buildTree(l_bound,r_bound):
                if self.idx == len(preorder):
                    return None
                
                if preorder[self.idx] < l_bound or preorder[self.idx] > r_bound:
                    return None
                
                node = TreeNode(preorder[self.idx])
                self.idx += 1
                node.left = buildTree(l_bound,node.val)
                node.right = buildTree(node.val,r_bound)
                return node
            
            return buildTree(float('-inf'),float('inf'))
        