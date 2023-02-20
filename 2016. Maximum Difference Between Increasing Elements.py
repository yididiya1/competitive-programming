class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        best = -1
        _min = nums[0]

        for i in range(len(nums)):
            best = max(best, nums[i] - _min)
            _min = min(_min, nums[i])

        if best != 0 :
            return best
        return -1
	    
        
