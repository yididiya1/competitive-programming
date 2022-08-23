class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        _sum = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            if _sum - left_sum - nums[i] == left_sum:
                return i
            left_sum += nums[i]
            
        return -1
        