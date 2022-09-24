# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        
        def dfs(node,p,q):
            if not node:
                return None

            if node.val == p or node.val == q:
                return node

            left = dfs(node.left,p,q)
            right = dfs(node.right,p,q)

            if left  and right :
                return node

            return left or right


        def commonStart(node,s):
            if not node:
                return []

            if node.val == s:
                return ['U']

            left = commonStart(node.left,s)
            right = commonStart(node.right,s)

            if left : left.append('U')
            if right : right.append('U')

            return left or right

        def commonDest(node,d,dxn):
            if not node:
                return []

            if node.val == d:
                return [dxn]


            left = commonDest(node.left,d,'L')
            right = commonDest(node.right,d,'R')

            if left: left.append(dxn)
            if right: right.append(dxn)

            # print(node.val,left,right)
            return left or right


        common = dfs(root,startValue,destValue)
        # print(common.val)
        up = commonStart(common,startValue)
        # print(up)
        up.pop()
        down = commonDest(common,destValue,'')
        # print(down)
        down.pop()
        down.reverse()
        x = up + down
        return "".join(x)

            
            
            