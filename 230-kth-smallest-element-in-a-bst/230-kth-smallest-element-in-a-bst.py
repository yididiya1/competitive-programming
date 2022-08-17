# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        
        stack = []
        result = []
        curr = root
        
        while stack or curr:
            if len(result) >= k:
                break
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
            
        return result[-1]
        
        