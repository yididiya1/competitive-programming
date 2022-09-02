class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        curr = nums[:-1].copy()
        
        def getMax(arr):

            @cache
            def dp(index):
                if index >= len(arr):
                    return 0
                rob = arr[index]+dp(index+2)
                not_rob = dp(index+1)

                return max(rob,not_rob)
            
            return dp(0)
       
        return max(getMax(nums[:-1]),getMax(nums[1:]))
        
        
        