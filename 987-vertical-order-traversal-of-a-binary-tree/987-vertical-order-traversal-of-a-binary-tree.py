# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_levels = defaultdict(list)
        
        def inorder(node,row,col):
            if not node:
                return 
            
            inorder(node.left,row+1,col-1)
            col_levels[col].append((row,node.val))
            inorder(node.right,row+1,col+1)
            
        
        inorder(root,0,0)
        output = []
        for key in sorted(col_levels.keys()):
            output.append([j[1]  for j in sorted(col_levels[key])])
            
        
        return output
        
        