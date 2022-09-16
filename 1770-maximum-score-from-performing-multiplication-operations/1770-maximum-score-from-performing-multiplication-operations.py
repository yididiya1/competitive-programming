class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        
        @lru_cache(2000)
        def dp(s,counter):
            if counter >= len(multipliers):
                return 0
            e = len(nums) - 1 - counter + s
            left = nums[s] * multipliers[counter]  + dp(s+1,counter + 1)
            right = nums[e] * multipliers[counter] + dp(s,counter + 1)
            
            return max(left,right)
        
        return dp(0,0)