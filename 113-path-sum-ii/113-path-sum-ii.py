# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        # self.result = []
        if not root:
            return []
        
        def dfs(node,_sum):
            
            if not node.left and not node.right:
                if _sum+node.val == targetSum:
                    # print("Found",node.val)
                    return [[node.val]]
                return []
            
            
            left_check =  dfs(node.left,_sum+node.val) if node.left else []
            right_check = dfs(node.right,_sum+node.val) if node.right else []
            
            # print(node.val,left_check,right_check)
            
            answer = []
            
            if left_check:
                for i in range(len(left_check)):
                    left_check[i].append(node.val)
            
            if right_check:
                for i in range(len(right_check)):
                    right_check[i].append(node.val)
            
            
            answer = left_check+right_check           
            return answer
        
        x = dfs(root,0)
        x = [j[::-1] for j in x]
        return x
        