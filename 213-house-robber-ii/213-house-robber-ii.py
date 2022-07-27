class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        if len(nums) == 1:
            return nums[0]
        
        def getMax(numss):
            
            memo = {}
            
            def dp(index):
                if index == len(numss) - 1:
                    return numss[index]
                if index == len(numss) - 2:
                    return max(numss[index+1],numss[index])

                if index in memo : return memo[index]

                rob = dp(index+2) + numss[index]
                not_rob = dp(index+1) + 0

                memo[index] = max(rob,not_rob)

                return max(rob,not_rob)

            return dp(0)
        
        return max(getMax(nums[1:]),getMax(nums[:-1]))
