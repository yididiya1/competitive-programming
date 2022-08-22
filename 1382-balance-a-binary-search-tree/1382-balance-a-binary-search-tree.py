# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.inorder_list = []
    
    def inorder(self,node):
        if not node:
            return
        
        self.inorder(node.left)
        self.inorder_list.append(node.val)
        self.inorder(node.right)
    def generateTree(self,l,r):
        if l > r:
            return 
        mid = (l+r)//2
        node = TreeNode(self.inorder_list[mid])
        
        if l == r:
            return node
        
        node.left = self.generateTree(l,mid-1)
        node.right = self.generateTree(mid+1,r)
        
        return node
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.inorder(root)
        return self.generateTree(0,len(self.inorder_list)-1)