# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            x = TreeNode(val)
            x.left = root
            return x
        
        queue = deque()
        queue.append((root,1))
        
        while queue:
            curr,d = queue.popleft()
            
            
            if curr:
                queue.append((curr.left,d+1))
                queue.append((curr.right,d+1))
            
            
                if d >= depth :
                    break
                else:
                    if  d == depth - 1:
                        left = TreeNode(val)
                        right = TreeNode(val)

                        temp1 = curr.left
                        temp2 = curr.right

                        curr.left = left
                        curr.right = right


                        left.left = temp1
                        right.right = temp2
                    
                    # break
                    
        return root
        
        
                
            
        