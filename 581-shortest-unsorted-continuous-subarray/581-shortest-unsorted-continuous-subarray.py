class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        _min = float('inf')
        _max = float('-inf')
        flag = False
        
        #get minimum number from the unsorted part
        for i in range(1,len(nums)):
            if nums[i - 1] > nums[i]:
                flag = True
            if flag:
                _min = min(_min,nums[i])
        
        flag = False
        
        #get maximum number once the unsorted part starts 
        for i in range(len(nums)-2,-1,-1):
            if nums[i+1] < nums[i]:
                flag = True
            if flag:
                _max = max(_max,nums[i])
                
        l = 0
        r = 0
        
        for i in range(len(nums)):
            l = i
            if nums[i] > _min:
                break
                
        for i in range(len(nums)-1,-1,-1):
            r = i
            if nums[i] < _max:
                break
        
        
        # print(r,l)
        if r - l <= 0:
            return 0
        return r - l + 1
        