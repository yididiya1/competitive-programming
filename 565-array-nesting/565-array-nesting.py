class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        self.best = 0
        
        visited = set()
        
        @cache
        def dfs(index):
            if index >= len(nums):
                return 0
            
            if index in visited:
                return 0
            
            visited.add(index)
            mine = 1 + dfs(nums[index])
            return mine
        
        for i in range(len(nums)):
            self.best = max(self.best,dfs(i))
            visited = set()
            
        return self.best
        
        
        
        