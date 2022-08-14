class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        l = 0
        r = 0
        curr = k
        _max = float('-inf')
        
        while r <= len(nums)-1:
            # print(l,r)
            if nums[r] == 1:
                r += 1
            else:
                if curr > 0:
                    r += 1
                    curr -= 1
                else:
                    _max = max(_max,r-l)
                    # print("Current ",r-l)
                    while nums[l] == 1:
                        l += 1
                    l += 1
                    curr += 1
        _max = max(_max,r-l)
        return _max
                    
        