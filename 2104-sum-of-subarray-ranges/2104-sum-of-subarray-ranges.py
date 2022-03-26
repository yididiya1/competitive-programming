class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            _min = nums[i]
            _max = nums[i]
            for j in range(i,len(nums)):
                _min = min(_min,nums[j])
                _max = max(_max,nums[j])
                total += _max - _min
                
                
        return total
        