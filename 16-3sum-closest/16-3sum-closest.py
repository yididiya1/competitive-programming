class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        def findTwoSum(i,targ):
            l = i
            r = len(nums)-1
            best = sum((nums[l],nums[r]))
            
            while l < r:
                curr = sum((nums[l],nums[r]))
                if abs(curr-targ) < abs(best-targ):
                    best = curr
                if curr < targ:
                    l += 1
                elif curr > targ:
                    r -= 1
                else:
                    break
            
            return best
            
        _min = float('inf')
        for i in range(len(nums)-2):
            x = findTwoSum(i+1,target-nums[i])
            # print(_min,x,x+nums[i])
            if abs((x+nums[i])-target) < abs(_min-target):
                _min = x + nums[i]
            
        return _min
        