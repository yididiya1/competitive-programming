class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        _max = 0
        nums = set(nums)
       
        for num in nums:
            if num-1 not in nums:
                start = num
                count = 1
                while start+1 in nums:
                    count += 1
                    start = start+1
                _max = max(count,_max)
                
        return _max
                    
        