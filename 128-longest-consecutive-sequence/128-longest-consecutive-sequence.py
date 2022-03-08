class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        _max = 0
        numbers = set(nums)
       
        for num in nums:
            if num-1 not in numbers:
                start = num
                count = 1
                while start+1 in numbers:
                    count += 1
                    start = start+1
                _max = max(count,_max)
                
        return _max
                    
        