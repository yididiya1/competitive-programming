class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        nums = [ -i for i in nums]
        

        for i in range(len(nums)):
            # print(nums)
            if nums[abs(nums[i])-1] > 0:
                return abs(nums[i])
            else:
                nums[abs(nums[i])-1] *= -1
        
