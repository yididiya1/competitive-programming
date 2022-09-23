class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        
        
        def backtrack(index,cur):
            if index >= len(nums):
                return 
            
            
            for i in range(index,len(nums)):
                cur.append(nums[i])
                x = cur.copy()
                output.append(x)
                backtrack(i+1,x)
                cur.pop()
                
        backtrack(0,[])
        return output
                
            