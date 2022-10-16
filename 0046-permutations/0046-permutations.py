class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.output = []
        
        def dfs(arr):
            if len(arr) == len(nums):
                self.output.append(arr)
                return 
            
            
            for n in nums:
                if n not in arr:
                    x  = arr.copy()
                    x.append(n)
                    dfs(x)
                    
        
        dfs([])
        return self.output
        